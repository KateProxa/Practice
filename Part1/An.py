!pip install transformers sentencepiece

from transformers import pipeline

translator = pipeline("translation_en_to_de", "Helsinki-NLP/opus-mt-en-de")

translator("Меня зовут Анастасия, я живу в Москве")
