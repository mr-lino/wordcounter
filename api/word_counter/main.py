from typing import Annotated

from fastapi import Body, FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

app = FastAPI()

ORIGINS = [
    "http://localhost:4173",
    "http://127.0.0.1:4173",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

METHODS = ["GET", "POST", "OPTIONS"]

HEADERS = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_methods=METHODS,
    allow_headers=HEADERS,
)


@app.get("/", status_code=status.HTTP_308_PERMANENT_REDIRECT)
async def root():
    return RedirectResponse("/docs")


@app.post("/word-count", status_code=status.HTTP_200_OK)
async def word_count(input_text: Annotated[str, Body(embed=True)]):
    return {"word_count": len(input_text.split())}
