# main.py
from typing import Optional

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import random
import string
import bcrypt

from utilClass.StockPrice import StockPrice


def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Params(BaseModel):
    length: int
    hashing: Optional[bool] = False


class StockParams(BaseModel):
    symbol: str
    interval: str
    data_format: Optional[str] = 'json'


app = FastAPI()


@app.get("/")
async def index():
    # Return the HTML file as a response
    return FileResponse("static/index.html")


@app.get("/speech")
async def index():
    # Return the HTML file as a response
    return FileResponse("static/speech.html")


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


@app.post("/get-stock-price-data")
async def index(params: StockParams):
    symbol = params.symbol
    interval = params.interval
    data_format = params.data_format
    ticker = StockPrice(symbol, interval, data_format)
    stock_data = ticker.get_stock_price_data()

    return stock_data
