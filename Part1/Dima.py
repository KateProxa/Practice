#Переводчик с русского на французский
from transformers import pipeline
model_ru2fr = pipeline("translation_ru_to_fr", model = "Helsinki-NLP/opus-mt-ru-fr")
result = model_ru2fr("всем привет меня зовут Дмитрий")
result
# Salut, tout le monde. Mon nom est Dimitri.
