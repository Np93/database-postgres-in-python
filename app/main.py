from fastapi import FastAPI, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from app.models import InputContent
from app.schemas import InputContentSchema
from app.database import init_db
from typing import List
from app.endpoints import Endpoint


app = FastAPI()

@app.on_event("startup")
async def startup_event():
    init_db(app)

# route personnel pour tester mon api
@app.get("/")
async def root():
    test = Endpoint.get_root()
    return test

# push dans ma database les valeur demander et execute la traduction et
#ainsi que rajoute le sentiment et la positiviter du sujet 
@app.post("/push_input_content/")
async def push_input_content(input_content: InputContentSchema):
    content_endpoint = Endpoint()
    return await content_endpoint.get_push_input_content(input_content)

# route personnel pour tester ma database
@app.get("/input_content/{input_content_id}", response_model=InputContentSchema, responses={404: {"model": HTTPNotFoundError}})
async def get_input_content(input_content_id: int):
   input_content = Endpoint()
   return await input_content.get_input_content_id(input_content_id)

# route personnel pour tester ma database
@app.get("/all_input_contents/", response_model=List[InputContentSchema])
async def get_all_input_contents():
    return await InputContent.all()

# calcule le sentiment median d'un sujet donner en paramettre
# et le retourne en float
@app.get("/get_median_sentiment_for_subject/{subject}")
async def get_median_sentiment_for_subject(subject: str):
    sentiments = Endpoint()
    return await sentiments.get_median_sentiment_for_subject_endpoint(subject)

@app.get("/get_subject/{type}")
async def get_subject(type: str):
    subject = Endpoint()
    return await subject.get_subject_endpoint(type)