# music-store-devops241_351# 🎵 Музыкальный магазин (music-store-devops241_351)

Учебный проект по дисциплине "Методология и практики DevOps".

## 📖 Описание
Веб-приложение для учета музыкальных дисков, управления каталогом исполнителей, оформления продаж и отслеживания остатков на складе. (версия Б)

## 👥 Команда
- Участник 1 — Backend/DB (модели, PostgreSQL, миграции)
- Участник 2 — API/Logic (FastAPI, бизнес-логика, авторизация)
- Участник 3 — Frontend/Docs/Git (шаблоны, документация, CI/CD)

## 🛠️ Стек технологий
- Python 3.11+
- FastAPI (HTTP API)
- PostgreSQL (БД)
- SQLAlchemy + Alembic (ORM и миграции)
- Jinja2 (шаблоны)
- Docker + Docker Compose (инфраструктура) 

## 📂 Структура проекта
music-store-devops241_351/
├── app/
│ ├── templates/ # HTML-шаблоны (Jinja2)
│ └── static/ # CSS, JS, изображения
├── docs/
│ └── TZ.md # Техническое задание
├── .env.example # Пример переменных окружения
├── .gitignore
├── CONTRIBUTING.md # Правила внесения изменений
└── README.md

## 🚀 Запуск проекта (будет дополнено)
1. Скопировать `.env.example` в `.env` и заполнить переменные.
2. Запустить базу данных:
   ```bash
   docker-compose up -d db
3. Применить миграции:
bash
alembic upgrade head
4. Запустить приложение:
bash
uvicorn app.main:app --reload
5. Открыть в браузере: http://localhost:8000

📊 Схема данных
(Будет добавлена после проектирования БД Участником 1)

🔗 Полезные ссылки
Swagger-документация API: http://localhost:8000/docs

Healthcheck: http://localhost:8000/health 