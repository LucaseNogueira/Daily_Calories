from abc import ABC, abstractmethod

class CalculaGEBAdapterPort(ABC):
    @abstractmethod
    def execute(self, peso:float, altura:float, idade:int, sexo:int)->float:
        '''Calcula o gasto energético basal (GEB) conforme o peso, altura e idade da pessoa.

        Example:
        - homem: (13,75 x peso em quilos) + (5 x altura em centímetros) – (6,76 x idade em anos) + 66,5
        
        Outputs
        - Gasto energético basal de uma pessoa
        '''
        pass