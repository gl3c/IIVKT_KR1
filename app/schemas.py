from pydantic import BaseModel
from typing import Optional, List

class GenerateRequest(BaseModel):
    prompt: str
    max_length: int = 300
    temperature: float = 0.85
    content_type: Optional[str] = None  # social, product, story, seo

class VariantsRequest(BaseModel):
    prompt: str
    max_length: int = 300
    temperature: float = 0.9
    num_variants: int = 3