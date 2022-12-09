from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from bot_brain import bot_searching
from pydantic import BaseModel

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    value: str

@app.post("/bot_searching")
def ranking_utter(item: Item):
    result = bot_searching(item.value.lower().replace('thủ tục',''))
    return {"ranking_answer": result}