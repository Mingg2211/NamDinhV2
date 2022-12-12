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

import re
def preprocessing(text):
    text = text.lower().replace('thủ tục','')
    text = re.sub(' +', ' ',text)
    text = re.sub(r'[^\s\wáàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệóòỏõọôốồổỗộơớờởỡợíìỉĩịúùủũụưứừửữựýỳỷỹỵđ_\.\,]',' ',text)
    return text


@app.post("/bot_searching")
def ranking_utter(item: Item):
    if item!='' and item:
        result = bot_searching(preprocessing(item.value))
    else:
        result = "Nhập lại nhé"
    return {"ranking_answer": result}