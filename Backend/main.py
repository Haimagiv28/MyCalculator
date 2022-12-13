import json
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
from models import *


class numbers(BaseModel):
    num1: float
    num2: float


app = FastAPI()


@app.get("/")
def welcome():
    return "Welcome to Haim's Calculator"


@app.post("/add")
def add_calc(numberTemp: numbers):
    return {"The sum is":  add(numberTemp.num1, numberTemp.num2)}


@app.post("/sub")
def sub_calc(numberTemp: numbers):
    return {"The sum is":  sub(numberTemp.num1, numberTemp.num2)}


@app.post("/multy")
def multy_calc(numberTemp: numbers):
    return {"The sum is":  multy(numberTemp.num1, numberTemp.num2)}


@app.post("/divide")
def divide_calc(numberTemp: numbers):
    return {"The sum is":  divide(numberTemp.num1, numberTemp.num2)}


@app.post("/pow")
def pow_calc(numberTemp: numbers):
    return {"Res: ":  power(numberTemp.num1, numberTemp.num2)}


@app.post("/linear_plot")
def linear_plot_calc(numberTemp: numbers):
    return {"Res :": linear_plot(numberTemp.num1, numberTemp.num2)}
