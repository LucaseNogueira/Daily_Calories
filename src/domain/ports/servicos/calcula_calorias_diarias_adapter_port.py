from abc import ABC, abstractmethod

class CalculaCaloriasDiariasAdapterPort(ABC):
    @abstractmethod
    def execute(self, geb:float, atividade_fisica:int)->float:
        pass