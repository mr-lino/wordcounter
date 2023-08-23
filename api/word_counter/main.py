from dataclasses import dataclass
from typing import Annotated
from fastapi import FastAPI, Body, status
from fastapi.responses import RedirectResponse


app = FastAPI()

@app.get("/")
async def root():
    return RedirectResponse("/docs")

@app.post("/word-count", status_code=status.HTTP_200_OK)
async def word_count(input_text: Annotated[str, Body(embed=True)]):

    return {"word_count": len(input_text.split())}