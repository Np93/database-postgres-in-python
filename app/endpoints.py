from app.schemas import InputContentSchema
from app.utils import Utils
from app.models import InputContent
from fastapi import HTTPException
import numpy as np  # Pour calculer la médiane
from collections import defaultdict

class Endpoint:

    def get_root():
        return {"Hello": "World"}

    async def get_push_input_content(self, input_content: InputContentSchema):
        translated_content = Utils.translate_content(input_content.content)
        subject = Utils.get_subject(translated_content)
        sentiment = Utils.compute_sentiment(translated_content)
        # Création et sauvegarde dans la base de données
        content_obj = await InputContent.create(title=input_content.title, source=input_content.source,
                                                timestamp=input_content.timestamp, content=input_content.content,
                                                translate_content=translated_content,
                                                subject=subject, sentiment=sentiment)
        return {"id": content_obj.id, "subject": subject, "sentiment": sentiment}

    async def get_input_content_id(self, input_content_id: int):
        input_content = await InputContent.get_or_none(id=input_content_id)
        if input_content is None:
            raise HTTPException(status_code=404, detail="InputContent not found")
        return input_content

    async def get_median_sentiment_for_subject_endpoint(self, subject: str):
        # Étape 1: Trouver les entrées correspondantes par le titre
        sentiments = await InputContent.filter(title=subject).values_list('sentiment', flat=True)
    
        if not sentiments:
            raise HTTPException(status_code=404, detail="No matching titles found")

        # Étape 2: Calculer le sentiment Median pour le retourner
        median_sentiment = np.median(sentiments) if sentiments else None
    
        return {
            median_sentiment
        }

    async def get_subject_endpoint(self, type: str):
        # Vérifier si le type demandé est "best" ou "worst"
        if type not in ["best", "worst"]:
            raise HTTPException(status_code=400, detail="Invalid type. Please use 'best' or 'worst'.")

        # Récupérer tous les contenus avec leurs titres et sentiments
        all_contents = await InputContent.all().values('title', 'sentiment')
    
        # Regrouper les sentiments par titre
        sentiments_by_title = defaultdict(list)
        for content in all_contents:
            sentiments_by_title[content['title']].append(content['sentiment'])
    
        # Calculer la médiane des sentiments pour chaque titre
        median_sentiments = {title: np.median(sentiments) for title, sentiments in sentiments_by_title.items()}
    
        # Trouver le titre avec la médiane de sentiment la plus élevée ou la plus basse
        if type == "best":
            selected_title = max(median_sentiments, key=median_sentiments.get)
        else:
            selected_title = min(median_sentiments, key=median_sentiments.get)

        return {selected_title}