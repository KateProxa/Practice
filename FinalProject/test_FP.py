from transformers import pipeline

def model(text):
    model_en2de = pipeline("translation_en_to_de", model = "Helsinki-NLP/opus-mt-en-de")
    return (model_en2de(text))

def test_1():
     assert model("I am student") == [{'translation_text': 'Ich bin Studentin'}]
#URFU
