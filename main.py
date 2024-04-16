from fastapi import FastAPI
from src.controllers.controller_api import ControllerApi

app = FastAPI()

@app.get('/dailycalories/')
def get_gasto_calorico_diario(sexo: int, peso: float, altura: float, idade: int, atividade_fisica: int):
    return ControllerApi.get_gasto_calorico_diario(sexo, peso, altura, idade, atividade_fisica)