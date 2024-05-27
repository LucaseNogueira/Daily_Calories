from src.domain.ports.servicos.calcula_calorias_diarias_adapter_port import CalculaCaloriasDiariasAdapterPort
from src.domain.ports.servicos.bo.bo_pessoa_adapter_port import BoPessoaAdapterPort

class CalculaCaloriasDiariasAdapter(CalculaCaloriasDiariasAdapterPort):

    def __init__(self, bo_pessoa_adapter:BoPessoaAdapterPort) -> None:
        self._bo_pessoa = bo_pessoa_adapter
        super().__init__()

    def execute(self, geb: float, atividade_fisica: int) -> float:
        return geb * self._bo_pessoa.fator_atividade_fisica(atividade_fisica)