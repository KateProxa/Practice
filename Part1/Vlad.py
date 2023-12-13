#Переводчик с английского на русский
from transformers import pipeline
model_en2ru = pipeline("translation_en_to_ru", model = "Helsinki-NLP/opus-mt-en-ru")
result = model_en2ru("I am student")
result
