from src.domain.ports.provedor.calcular_calorias_diarias_use_case_port import CalcularCaloriasDiariasUseCasePort
from src.domain.models.pessoa import Pessoa
from src.domain.ports.servicos.calcula_geb_adapter_port import CalculaGEBAdapterPort
from src.domain.ports.servicos.calcula_calorias_diarias_adapter_port import CalculaCaloriasDiariasAdapterPort

class CalcularCaloriasDiariasUseCase(CalcularCaloriasDiariasUseCasePort):

    def __init__(self, calcula_geb_adapter:CalculaGEBAdapterPort, calcula_calorias_adapter:CalculaCaloriasDiariasAdapterPort) -> None:
        self._calcular_geb = calcula_geb_adapter
        self._calcular_calorias = calcula_calorias_adapter
        super().__init__()

    def execute(self, pessoa: Pessoa) -> float:
        geb_calculado = self._calcular_geb.execute(pessoa.peso,pessoa.altura,pessoa.idade,pessoa.sexo)
        return self._calcular_calorias.execute(geb_calculado, pessoa.atividade_fisica)