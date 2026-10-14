#!/bin/bash
# Скрипт первичной настройки сервера приложения.
# Устанавливает пакеты, создаёт пользователя, клонирует репозиторий, настраивает ufw.

set -e

REPO_URL="https://github.com/Sandr192/music-store-devops241_351.git"
APP_USER="appuser"
APP_DIR="/home/${APP_USER}/app"

echo "===> Обновление системы"
sudo apt update && sudo apt upgrade -y

echo "===> Установка базовых пакетов"
sudo apt install -y python3 python3-venv python3-dev libpq-dev build-essential git curl ufw

echo "===> Создание системного пользователя ${APP_USER}"
if ! id "${APP_USER}" &>/dev/null; then
    sudo adduser --system --group --home "/home/${APP_USER}" --shell /bin/bash "${APP_USER}"
else
    echo "Пользователь ${APP_USER} уже существует, пропускаем."
fi

echo "===> Клонирование репозитория в ${APP_DIR}"
if [ ! -d "${APP_DIR}" ]; then
    sudo -u "${APP_USER}" git clone "${REPO_URL}" "${APP_DIR}"
else
    echo "Директория ${APP_DIR} уже существует, пропускаем клонирование."
fi

echo "===> Создание venv и установка зависимостей"
sudo -u "${APP_USER}" bash -c "cd ${APP_DIR} && python3 -m venv venv && source venv/bin/activate && pip install --upgrade pip"

echo "===> Настройка firewall (ufw)"
sudo ufw allow 22/tcp
sudo ufw allow 8000/tcp
sudo ufw --force enable

echo "===> Проверка статуса ufw"
sudo ufw status verbose

echo "===> Provisioning завершён успешно!"
echo "Не забудь создать ${APP_DIR}/.env с DATABASE_URL и SECRET_KEY."