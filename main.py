from fastapi import FastAPI, Depends
from src.adapters.provedor.routes.calcular_calorias_diarias_route import CalcularCaloriasDiariasRoute

app = FastAPI()

# Define o esquema OAuth2 com Bearer Token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get('/dailycalories/')
def get_gasto_calorico_diario(sexo: int, peso: float, altura: float, idade: int, atividade_fisica: int, token: str = Depends(oauth2_scheme)):
    return CalcularCaloriasDiariasRoute.get_gasto_calorico_diario(sexo, peso, altura, idade, atividade_fisica, token)