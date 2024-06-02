from src.domain.models.pessoa import Pessoa
from src.adapters.interfaces.requests.request_interface import RequestInterface

class CalcularCaloriasDiariasRequest(RequestInterface):

    def __init__(self, sexo: int, peso: float, altura: float, idade: int, atividade_fisica: int) -> None:
        self._sexo = sexo
        self._peso = peso
        self._altura = altura
        self._idade = idade
        self._atividade_fisica = atividade_fisica

    def to_domain(self):
        self._valida_sexo()
        self._valida_peso()
        self._valida_altura()
        self._valida_idade()
        self._valida_atividade_fisica()
        return Pessoa(self._sexo,self._peso,self._altura,self._idade,self._atividade_fisica)
    
    def _valida_sexo(self)->None:
        if self._sexo not in range(1,3):
            raise ValueError("Valor invalido para o atributo sexo. Insira 1 para feminino e 2 para masculino")
    
    def _valida_peso(self)->None:
        if self._peso <= 0:
            raise ValueError("Valor invalido para o atributo peso. Insira um valor maior que 0 (zero)")
        
    def _valida_altura(self)->None:
        if self._altura <= 0:
            raise ValueError("Valor invalido para o atributo altura. Insira um valor maior que 0 (zero)")
        
    def _valida_idade(self)->None:
        if self._idade <= 0:
            raise ValueError("Valor invalido para o atributo idade. Insira um valor maior que 0 (zero)")
    
    def _valida_atividade_fisica(self)->None:
        if self._atividade_fisica not in range(1,6):
            raise ValueError("Valor invalido para o atributo atividade_fisica. Insira um 1 para sedentário, 2 para levemente ativo, 3 para moderadamente ativo, 4 muito ativo, 5 extremamente ativo.")