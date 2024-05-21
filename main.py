from fastapi import FastAPI
from src.controllers.controller_api import ControllerApi
from src.models.message import MessageSucesso, MessageInternaServerlError
from src.utils.log_request import LogRequest

app = FastAPI()

@app.get('/dailycalories/')
def get_gasto_calorico_diario(sexo: int, peso: float, altura: float, idade: int, atividade_fisica: int):
    try:
        pessoa_json =  ControllerApi.get_gasto_calorico_diario(sexo, peso, altura, idade, atividade_fisica)
        message = MessageSucesso('Requisição realizada com sucesso!')
        message.set_body(pessoa_json)
        return message.to_dict
    except Exception:
        message = MessageInternaServerlError('Ocorreu uma falha interna no servidor')
        log = LogRequest(message)
        log.cadastrar
        return message.to_dict