# Pyrotech Calculator

Инструмент для расчёта окислительного баланса пиротехнических составов.  
Используется инженерами для подбора оптимального соотношения окислителя и горючего.

## Возможности
- Расчёт массовых долей по заданному ОБ
- Поддержка базы компонентов (PostgreSQL / Excel)
- Desktop-приложение (Tkinter)
- REST API (FastAPI) с OpenAPI-документацией
- Автоматические тесты

## Технологии
- Python 3.10+
- FastAPI, uvicorn
- psycopg2, openpyxl
- SymPy (численные расчёты)
- pytest

## Запуск
1. Установите зависимости: `pip install -r requirements.txt`
2. Задайте подключение к БД в файле conf.py
3. Заполните БД: `python scripts/load_to_db.py`
4. GUI: `python main.py`
5. API: `python api_server.py` → [http://localhost:8000/docs](http://localhost:8000/docs)

## Пример API-запроса
```bash
curl -X POST http://localhost:8000/api/v1/calculate \
  -H "Content-Type: application/json" \
  -d '{"oxidizer_id":1,"fuel_id":1,"balance":0}'# Pyro_calculator-1.0
