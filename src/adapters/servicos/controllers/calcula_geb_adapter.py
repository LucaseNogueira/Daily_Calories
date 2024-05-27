from src.domain.ports.servicos.calcula_geb_adapter_port import CalculaGEBAdapterPort
from src.domain.ports.servicos.bo.bo_pessoa_adapter_port import BoPessoaAdapterPort

class CalculaGEBAdapter(CalculaGEBAdapterPort):

    def __init__(self, bo_pessoa_adapter:BoPessoaAdapterPort) -> None:
        self._bo_pessoa = bo_pessoa_adapter
        super().__init__()

    def execute(self, peso:float, altura:float, idade:int, sexo:int)->float:
        resposta = self._bo_pessoa.fator_peso(sexo) * peso
        resposta += self._bo_pessoa.fator_altura(sexo) * altura
        resposta -= self._bo_pessoa.fator_idade(sexo) * idade
        resposta += 66.5 if sexo == 1 else 665
        return resposta