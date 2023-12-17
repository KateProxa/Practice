# API Translator (FastAPI)

Приложение-переводчик с русского языка на французский

## Модель машинного обучения

[Описание модели](https://huggingface.co/Helsinki-NLP/opus-mt-ru-fr)

## Запуск приложения:

1. Создать виртуальное окружение:

    `python3 -m venv env`

2. Активировать виртуальное окружение:

    `source env/bin/activate`

3. Перейти в Practice/Part3/Translator
   
    `cd Practice/Part3/Translator`
   
4. Установить зависимости:

    `pip install -r requirements.txt`
   
5. Запустить приложение:

    `uvicorn main:app`

6. Cформировать POST запрос

    `curl -X 'POST' 'http://127.0.0.1:8000/predict/' -H 'Content-Type: application/json' -d '{"text": "Скоро будет зима"}'`
   
