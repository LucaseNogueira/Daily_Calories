from src.domain.models.pessoa import Pessoa
from src.adapters.interfaces.requests.request_interface import RequestInterface

class CalcularCaloriasDiariasRequest(RequestInterface):

    def __init__(self, sexo: int, peso: float, altura: float, idade: int, atividade_fisica: int) -> None:
        self._pessoa = Pessoa(sexo,peso,altura,idade,atividade_fisica)

    def to_domain(self):
        return self._pessoa