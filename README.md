# Инструкция по запуску

## 1. Клонирование репозитория: 
```
git clone git@github.com:lebedevAr/FastAPI.git
```

## 2. Установка requirements.txt
```
cd FastAPI/
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 3. Запуск сервера
```
cd app/
python3 -m uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```
**Тестирование:** Команда выполняется находясь в директории FastAPI/
```
pytest test.py
```
