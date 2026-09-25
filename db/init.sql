-- 1. Включаем поддержку внешних ключей
PRAGMA foreign_keys = ON;

-- 2. Удаляем старые таблицы, если они есть
DROP TABLE IF EXISTS sales;
DROP TABLE IF EXISTS album_genres;
DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS genres;
DROP TABLE IF EXISTS musicians;

-- 3. Создаём таблицу музыкантов
CREATE TABLE musicians (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    country VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. Создаём таблицу жанров
CREATE TABLE genres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) UNIQUE NOT NULL
);

-- 5. Создаём таблицу альбомов
CREATE TABLE albums (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(255) NOT NULL,
    release_year INTEGER,
    price NUMERIC(10, 2) NOT NULL,
    stock_quantity INTEGER NOT NULL DEFAULT 0,
    musician_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_album_musician FOREIGN KEY (musician_id) 
        REFERENCES musicians(id) ON DELETE CASCADE,
    CONSTRAINT check_price_positive CHECK (price >= 0),
    CONSTRAINT check_stock_positive CHECK (stock_quantity >= 0)
);

-- 6. Создаём связующую таблицу альбомов и жанров (многие-ко-многим)
CREATE TABLE album_genres (
    album_id INTEGER NOT NULL,
    genre_id INTEGER NOT NULL,
    PRIMARY KEY (album_id, genre_id),
    CONSTRAINT fk_album_genre_album FOREIGN KEY (album_id) 
        REFERENCES albums(id) ON DELETE CASCADE,
    CONSTRAINT fk_album_genre_genre FOREIGN KEY (genre_id) 
        REFERENCES genres(id) ON DELETE CASCADE
);

-- 7. Создаём таблицу продаж
CREATE TABLE sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    album_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    total_price NUMERIC(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_sale_album FOREIGN KEY (album_id) 
        REFERENCES albums(id) ON DELETE RESTRICT,
    CONSTRAINT check_sale_quantity CHECK (quantity > 0),
    CONSTRAINT check_sale_total_price CHECK (total_price >= 0)
);