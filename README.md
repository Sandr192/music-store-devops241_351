## 🎵 Музыкальный магазин (music-store-devops241_351)

Учебный проект по дисциплине "Методология и практики DevOps".

## 📖 Описание
Веб-приложение для учета музыкальных дисков, управления каталогом исполнителей, оформления продаж и отслеживания остатков на складе.

## 👥 Команда
- Участник 1 — Backend/DB (модели, SQLiteStudio, миграции)
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

```text
music-store-devops241_351/
├── app/
│   ├── templates/        # HTML-шаблоны (Jinja2)
│   └── static/           # CSS, JS, изображения
├── docs/
│   └── TZ.md             # Техническое задание
├── .env.example          # Пример переменных окружения
├── .gitignore
├── CONTRIBUTING.md       # Правила внесения изменений
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

## 📊 Схема данных

### Таблицы
- **musicians** — музыканты (id, name, country, created_at)
- **genres** — жанры (id, name)
- **albums** — альбомы (id, title, release_year, price, stock_quantity, musician_id, created_at)
- **album_genres** — связь альбомов и жанров (album_id, genre_id)
- **sales** — продажи (id, album_id, quantity, total_price, created_at)

### Связи
- `albums.musician_id` → `musicians.id` (многие-к-одному)
- `album_genres` — многие-ко-многим между `albums` и `genres`
- `sales.album_id` → `albums.id` (многие-к-одному)

### Бизнес-правила
- Цена и остаток альбома не могут быть отрицательными.
- Количество продажи > 0, итоговая цена >= 0.

🔗 Полезные ссылки
Swagger-документация API: http://localhost:8000/docs

Healthcheck: http://localhost:8000/health 