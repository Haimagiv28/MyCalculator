import json
from fastapi import FastAPI
from pydantic import BaseModel
from models import *
import httptools


class numbers(BaseModel):
    num1: float
    num2: float


app = FastAPI()


@app.get("/")
def welcome():
    return "Welcome to Haim's Calculator"


@app.post("/add")
def add_calc(numberBase: numbers):
    return {add(numberBase.num1, numberBase.num2)}


@app.post("/sub")
def sub_calc(numberBase: numbers):
    return {sub(numberBase.num1, numberBase.num2)}


@app.post("/multy")
def multy_calc(numberBase: numbers):
    return {multy(numberBase.num1, numberBase.num2)}


@app.post("/divide")
def divide_calc(numberBase: numbers):
    return {divide(numberBase.num1, numberBase.num2)}


@app.post("/pow")
def pow_calc(numberBase: numbers):
    return {power(numberBase.num1, numberBase.num2)}


@app.post("/linear_plot")
def linear_plot_calc(numberBase: numbers):
    return {"Res": linear_plot(numberBase.num1, numberBase.num2)}


@app.post("/percent")
def percentXofY_calc(numberBase: numbers):
    return {percent(numberBase.num1, numberBase.num2)}
