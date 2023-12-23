import io
import streamlit as st
from transformers import pipeline
@st.cache_resource
def load_model():
    return pipeline("translation_en_to_de", model = "Helsinki-NLP/opus-mt-en-de")
translation = load_model()
st.title('Translator to Deutch')
st.write('Это приложение для перевода текста на немецкий язык')
text = st.text_area('Введите текст для перевода на английском языке')
result = st.button('Перевести')
if result:
    tr_text = translation(text)
    st.write("Перевод:", tr_text[0]['translation_text'])
