from pydantic import BaseModel

class InputContentSchema(BaseModel):
    title: str
    source: str
    timestamp: str
    content: str