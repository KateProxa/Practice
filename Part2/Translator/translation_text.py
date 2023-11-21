import io
import streamlit as st
from transformers import pipeline


@st.cache_resource
#@st.cache_data
# загружаю модель
def load_model():
    return pipeline("translation_ru_to_fr", model = "Helsinki-NLP/opus-mt-ru-fr")

translation = load_model()

# Вывожу заголовок страницы средствами Streamlit
st.title('Translator from Russian to French')

st.write('Это приложение для перевода текста с русского языка на французский')

text = st.text_area('Введите текст для перевода', 'Скоро наступит Новый Год!')

# Кнопка для запуска
result = st.button('Перевести')
# Если кнопка нажата, то запускаем
if result:
    tr_text = translation(text)
    st.write("Перевод:", tr_text[0]['translation_text'])
#    tr_text.clear()
