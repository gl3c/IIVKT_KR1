from transformers import pipeline
import torch
from typing import Optional

generator = None

def get_generator():
    global generator
    if generator is None:
    
        
        generator = pipeline(
            "text-generation",
            model="sberbank-ai/rugpt3large_based_on_gpt2",   # ← самая лучшая из маленьких
            device=0 if torch.cuda.is_available() else -1,
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
        )
    return generator

def prepare_prompt(user_input: str, content_type: Optional[str]) -> str:
    theme = user_input.strip()
    
    # Few-shot примеры — модель гораздо лучше понимает задачу
    examples = {
        "social": "Пример: Тема: кофе по утрам\nПост: ☕ Доброе утро! Сегодня мой кофе пахнет приключениями и свежим началом дня. А какой у вас любимый ритуал по утрам? ✨",
        "product": "Пример: Тема: беспроводные наушники\nОписание: Лёгкие, с отличным звуком и 30 часами работы. Идеально для спорта, работы и путешествий.",
        "story": "Пример: Тема: потерянный ключ\nРассказ: Однажды дождливым вечером парень нашёл старый ключ в кармане куртки...",
        "seo": "Пример: Тема: кофе\nЗаголовки:\n1. 10 причин, почему кофе по утрам меняет вашу жизнь\n2. Как выбрать лучший кофе в 2025 году"
    }
    
    system = f"Ты — профессиональный копирайтер 2025 года. Пиши ТОЛЬКО чистый оригинальный текст по теме. Никаких дат, номеров, конкурсов, старых постов и мусора.\n\nПример:\n{examples.get(content_type, '')}\n\nТеперь тема: {theme}\n"
    
    if content_type == "social":
        return system + "Напиши ОДИН яркий пост для соцсетей с эмодзи."
    elif content_type == "product":
        return system + "Напиши продающее описание товара."
    elif content_type == "story":
        return system + "Напиши короткий увлекательный рассказ."
    elif content_type == "seo":
        return system + "Придумай 6–8 ярких SEO-заголовков. Каждый с новой строки."
    else:
        return system + "Напиши качественный текст по теме."