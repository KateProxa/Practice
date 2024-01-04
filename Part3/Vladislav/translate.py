#Телегинский Владислав Владиславович
from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    text: str

translate=pipeline("translation_en_to_ru", model = "Helsinki-NLP/opus-mt-en-ru")

@app.post("/predict/")
async def predict(item: Item):
    return translate(item.text)[0]
