from fastapi import FastAPI
from pydantic import BaseModel
from utils import message_to_chat_gpt
from fastapi.responses import JSONResponse

from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI
app = FastAPI()

app = FastAPI(
    title = "API",
    description = "A simple API",
    version = "0.1",
)

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_methods = ["*"],
)

@app.get("/ok")
async def ok_endpoint():
    return {"message": "ok"}

@app.get('/')
def index():
    return {"Msg": "go to /docs for the API documentation"}

@app.get("/hello")
async def hello_endpoint(name: str = 'World'):
    return JSONResponse(content = {"Name": name}, status_code = 200)


class Message(BaseModel):
    notes: str

@app.post("/chat")
async def message(message: Message):
    message = message_to_chat_gpt(message.notes)

    get_messsage = message
    return {"message": message}


@app.get("/message")
async def message(message):
    return {"message": message}


'''
- React js
- FastAPI
- JavaScript
- JSX
- CORS FastAPI
- ES6 syntax
- Python
- Pydantic models
-  CRUD API
- Tortoise ORM
- Pydantic Models
- FastAPI-mail
'''