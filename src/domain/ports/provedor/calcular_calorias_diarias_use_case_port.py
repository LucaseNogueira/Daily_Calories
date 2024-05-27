from abc import ABC, abstractmethod
from src.domain.models.pessoa import Pessoa

class CalcularCaloriasDiariasUseCasePort(ABC):
    @abstractmethod
    def execute(self, pessoa:Pessoa)->float:
        '''Calcula as calorias diárias da pessoa setada na calculadora

        Example:
        - homem: GEB * 66.5

        Outputs:
        - Calorias diárias calculada
        '''
        pass