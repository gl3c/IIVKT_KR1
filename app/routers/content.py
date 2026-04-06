from fastapi import APIRouter
from ..schemas import GenerateRequest, VariantsRequest
from ..generator import get_generator, prepare_prompt

router = APIRouter()

def clean_text(text: str) -> str:
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    cleaned = []
    for line in lines:
        lower = line.lower()
        if any(x in lower for x in ['2015','2016','202','http','@','rss','конкурс','балл','рейтинг','бонус','серпокрылов','marija','пример:']):
            continue
        if line[0].isdigit() and len(line.split()) < 12:
            continue
        cleaned.append(line)
    return '\n\n'.join(cleaned).strip()

@router.post("/generate")
async def generate(req: GenerateRequest):
    gen = get_generator()
    full_prompt = prepare_prompt(req.prompt, req.content_type)
    
    result = gen(
        full_prompt,
        max_length=req.max_length,
        temperature=0.65,
        do_sample=True,
        top_p=0.85,
        top_k=50,
        repetition_penalty=1.7,
        no_repeat_ngram_size=4,
        num_return_sequences=1,
        pad_token_id=gen.tokenizer.eos_token_id
    )
    
    text = result[0]['generated_text'][len(full_prompt):].strip()
    return {"generated_text": clean_text(text), "full_prompt": full_prompt}

@router.post("/generate/variants")
async def generate_variants(req: VariantsRequest):
    gen = get_generator()
    full_prompt = prepare_prompt(req.prompt, None)
    
    results = gen(
        full_prompt,
        max_length=req.max_length,
        temperature=0.68,
        do_sample=True,
        top_p=0.85,
        top_k=50,
        repetition_penalty=1.7,
        no_repeat_ngram_size=4,
        num_return_sequences=req.num_variants,
        pad_token_id=gen.tokenizer.eos_token_id
    )
    
    variants = [clean_text(r['generated_text'][len(full_prompt):].strip()) for r in results]
    return {"variants": variants, "full_prompt": full_prompt}