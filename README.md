# AI Content Generator

**Контрольная работа №1** — API для генерации контента с помощью локальной русской языковой модели

![Python](https://img.shields.io/badge/Python-3.12+-blue?style=flat-square)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green?style=flat-square)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Transformers-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue.svg)

## 📋 О проекте

Веб-приложение с удобным интерфейсом, которое позволяет пользователю ввести тему или ключевые слова и быстро получить качественный контент на русском языке с помощью мощной **локальной** модели ИИ.

**Генерирует:**
- Посты для социальных сетей (VK, Telegram, Instagram)
- Продающие описания товаров
- Короткие увлекательные рассказы
- SEO-заголовки

## ✨ Возможности

- Современный и responsive веб-интерфейс
- Выбор типа контента
- Генерация одного или нескольких вариантов
- Регулировка длины текста и креативности (temperature)
- Полностью локальная работа (после первой загрузки модели интернет не требуется)
- Автоматическая очистка текста от «мусора» модели

## 🚀 Быстрый запуск

### 1. Клонируйте репозиторий
```bash
git clone https://github.com/ВАШ_НИК/ai-content-generator.git
cd ai-content-generator
```



2. Создайте виртуальное окружение
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
# source venv/bin/activate
```

3. Установите зависимости
```bash
pip install -r requirements.txt

# PyTorch для CPU
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

4. Запустите проект
```bash
python run.py


Откройте в браузере: http://127.0.0.1:8000
```


🛠 Технологии

FastAPI — современный высокопроизводительный веб-фреймворк

Hugging Face Transformers — работа с языковыми моделями

ruGPT-3 Large (sberbank-ai/rugpt3large_based_on_gpt2) — лучшая открытая русская модель

Jinja2 + Tailwind CSS — красивый фронтенд

Pydantic — валидация данных



📁 Структура проекта


```bash
ai-content-generator/
├── run.py                  # Запуск сервера
├── requirements.txt
├── app/
│   ├── main.py             # Основное FastAPI приложение
│   ├── schemas.py          # Pydantic модели
│   ├── generator.py        # Логика генерации и промпты
│   ├── routers/
│   │   └── content.py      # Эндпоинты API
│   └── templates/
│       └── index.html      # Веб-интерфейс
```

📡 API Эндпоинты


POST /generate — генерация одного варианта контента

POST /generate/variants — генерация нескольких вариантов

Документация API:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc
