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

---
## Работа с API

1. Открыть в браузере страницу с документацией `http://127.0.0.1:8000/docs`
   ![1 Скриншот](https://github.com/KateProxa/Practice/blob/main/Part3/Translator/img/1%20skrin.jpg)
2. Открыть поле для ввода POST запроса
3. Нажать кнопку `Try it out`
   ![2 Скриншот](https://github.com/KateProxa/Practice/blob/main/Part3/Translator/img/2%20skrin.jpg)
4. Ввести в поле вместо `srting` текст для перевода
   ![3 Скриншот](https://github.com/KateProxa/Practice/blob/main/Part3/Translator/img/3%20skrin.jpg)
5. Нажать кнопку `Execute`
   ![4 Скриншот](https://github.com/KateProxa/Practice/blob/main/Part3/Translator/img/4%20skrin.jpg)
6. Готово! В поле ниже будет отображаться результат
   ![5 Скриншот](https://github.com/KateProxa/Practice/blob/main/Part3/Translator/img/5%20skrin.jpg)
   
