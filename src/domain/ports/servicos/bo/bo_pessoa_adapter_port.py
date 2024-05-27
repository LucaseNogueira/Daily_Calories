from abc  import ABC, abstractmethod

class BoPessoaAdapterPort(ABC):
    @abstractmethod
    def fator_peso(self, sexo:int)->float:
        pass

    @abstractmethod
    def fator_altura(self, sexo:int)->float:
        pass

    @abstractmethod
    def fator_idade(self, sexo:int)->float:
        pass

    @abstractmethod
    def fator_atividade_fisica(self, atividade_fisica:int)->float:
        pass