from fastapi import FastAPI, Depends
from src.adapters.provedor.routes.calcular_calorias_diarias_route import CalcularCaloriasDiariasRoute
from fastapi.security import OAuth2PasswordBearer
from prometheus_fastapi_instrumentator import Instrumentator
from fastapi.openapi.utils import get_openapi
import os
from dotenv import load_dotenv

load_dotenv()
env = os.getenv("ENV")

from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

Instrumentator().instrument(app).expose(app)

# Define o esquema OAuth2 com Bearer Token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

if env == "dev":
    def custom_openapi():
        openapi_schema = get_openapi(
            title="API DailyCalories",
            version="1.0.0",
            description="documentação da Api de Calorias diárias",
            routes=app.routes,
        )
        return openapi_schema

    app.openapi = custom_openapi

@app.get('/dailycalories/', tags=["dailycalories"], summary="Calcula calorias diárias de alimentos")
def get_gasto_calorico_diario(sexo: int, peso: float, altura: float, idade: int, atividade_fisica: int, token: str = Depends(oauth2_scheme)):

    """
    Endpoint para calcular o gasto calórico diário com base nos parâmetros informados.
    """
    return CalcularCaloriasDiariasRoute.get_gasto_calorico_diario(sexo, peso, altura, idade, atividade_fisica, token)

