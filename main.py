# main.py
from typing import Optional

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import random
import string
import bcrypt


def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Params(BaseModel):
    length: int
    hashing: Optional[bool] = False
    tax: Optional[float] = None


app = FastAPI()


@app.get("/")
async def index():
    # Return the HTML file as a response
    return FileResponse("static/index.html")


@app.post("/generate-password")
async def create_item(params: Params):
    if params.length < 12:
        return {"error": "Minimum length for a secure password is 12."}

    characters = string.ascii_letters + string.digits + string.punctuation  # includes uppercase letters, lowercase letters, digits, and punctuation symbols

    # Generate multiple random characters
    random_chars = random.choices(characters, k=params.length)

    # Concatenate random_chars into a string
    random_string = ''.join(random_chars)

    if params.hashing:
        random_string = hash_password(random_string)

    return {
        "generated_password": random_string
    }