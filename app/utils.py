from random import random

class ListDatabase:
    def __init__(self):
        self.elements = []

    def store(self, elem) -> int:
        self.elements.append(elem)
        return len(self.elements) - 1
    
    def get(self, id: int):
        return self.elements[id]

class Utils:
    db = None

    def get_database():
        if not Utils.db:
            Utils.db = ListDatabase()
        return Utils.db
    
    def get_subject(content):
        """Simulate subject calculation, no need to implement this."""
        return "sample subject"
    
    def compute_sentiment(content) -> float:
        """Simulate sentiment computation, no need to implement this."""
        return random()
    
    def translate_content(content: str) -> str:
        """Simulate text translation, no need to implement this."""
        return "<translated text>"