#Переводчик с русского на французский
from transformers import pipeline
model_ru2fr = pipeline("translation_ru_to_fr", model = "Helsinki-NLP/opus-mt-ru-fr")
result = model_ru2fr("Скоро наступит Новый Год!")
# C'est bientôt le Nouvel An !
