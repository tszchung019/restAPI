# main.py
from typing import Optional

from fastapi import FastAPI
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


@app.post("/generate-password")
async def create_item(params: Params):
    characters = string.ascii_letters + string.digits + string.punctuation  # includes uppercase letters, lowercase letters, digits, and punctuation symbols

    # Generate multiple random characters
    random_chars = random.choices(characters, k=params.length)  # Generate 5 random characters

    # Concatenate random_chars into a string
    random_string = ''.join(random_chars)

    if params.hashing:
        random_string = hash_password(random_string)

    return {
        "generated_password": random_string
    }