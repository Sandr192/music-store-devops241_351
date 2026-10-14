#!/bin/bash
# Скрипт обновления приложения на сервере.
# Обновляет код, зависимости, миграции и перезапускает systemd-службу.

set -e

APP_DIR="/home/appuser/app"
SERVICE_NAME="music-store"

echo "===> Переход в директорию приложения: ${APP_DIR}"
cd "$APP_DIR"

echo "===> Обновление кода из репозитория (git pull)"
sudo -u appuser git pull origin main

echo "===> Активация venv и установка зависимостей"
sudo -u appuser bash -c "cd ${APP_DIR} && source venv/bin/activate && pip install -r requirements.txt"

echo "===> Применение миграций Alembic"
sudo -u appuser bash -c "cd ${APP_DIR} && source venv/bin/activate && alembic upgrade head"

echo "===> Перезапуск systemd-службы: ${SERVICE_NAME}"
sudo systemctl restart "${SERVICE_NAME}"

echo "===> Статус службы"
sudo systemctl status "${SERVICE_NAME}" --no-pager

echo "===> Развёртывание завершено успешно!"