from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from .routers import content
from .generator import get_generator
import os

app = FastAPI(title="AI Content Generator", version="1.0")


app.include_router(content.router)


@app.get("/", response_class=HTMLResponse)
async def home():
    file_path = os.path.join("app", "templates", "index.html")
    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)


@app.on_event("startup")
async def startup_event():
    get_generator()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)