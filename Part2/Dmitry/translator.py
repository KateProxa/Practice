
import io
import streamlit as st
from transformers import pipeline

@st.cache_resource

# Функция для загрузки готовой модели 
def load_model():
    return pipeline("translation_ru_to_fr", model = "Helsinki-NLP/opus-mt-ru-fr")

# Загружаем предварительно обученную модель
translation = load_model()

# Выводим заголовок страницы
st.title('Translator from French to Russian')

#st.write('Это приложение для перевода текста с английского языка на русский')

# поле для ввода текста
ru_text = st.text_area('Введите текст')

# кнопка для запуска перевода
result = st.button('Перевести')

# Запуск
if result:
    fr_text = translation(ru_text)
    st.write("Перевод:", fr_text[0]['translation_text'])
