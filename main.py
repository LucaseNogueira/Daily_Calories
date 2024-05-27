from fastapi import FastAPI
from src.adapters.provedor.routes.calcular_calorias_diarias_route import CalcularCaloriasDiariasRoute

app = FastAPI()

@app.get('/dailycalories/')
def get_gasto_calorico_diario(sexo: int, peso: float, altura: float, idade: int, atividade_fisica: int):
    return CalcularCaloriasDiariasRoute.get_gasto_calorico_diario(sexo, peso, altura, idade, atividade_fisica)