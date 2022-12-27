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
def add_calc(numberBase: numbers):
    return {"Res":  add(numberBase.num1, numberBase.num2)}


@app.post("/sub")
def sub_calc(numberBase: numbers):
    return {"Res":  sub(numberBase.num1, numberBase.num2)}


@app.post("/multy")
def multy_calc(numberBase: numbers):
    return {"Res":  multy(numberBase.num1, numberBase.num2)}


@app.post("/divide")
def divide_calc(numberBase: numbers):
    return {"Res":  divide(numberBase.num1, numberBase.num2)}


@app.post("/pow")
def pow_calc(numberBase: numbers):
    return {"Res:":  power(numberBase.num1, numberBase.num2)}


@app.post("/linear_plot")
def linear_plot_calc(numberBase: numbers):
    return {"Res:": linear_plot(numberBase.num1, numberBase.num2)}
