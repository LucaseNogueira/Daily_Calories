
class Pessoa:

    def __init__(self, sexo:int, peso:float, altura:float, idade:int, atividade_fisica:int):
        self._sexo = sexo
        self._peso = peso
        self._altura = altura
        self._idade = idade
        self._atividade_fisica = atividade_fisica
        self._fator_peso = None
        self._fator_altura = None
        self._fator_idade = None
        self._fator_atividade_fisica = None

    @property
    def sexo(self):
        return self._sexo

    @property
    def peso(self):
        return self._peso

    @property
    def altura(self):
        return self._altura

    @property
    def idade(self):
        return self._idade

    @property
    def fator_peso(self):
        if self._fator_peso == None:
            if self._sexo == 1:
                self._fator_peso = 13.75
            else:
                self._fator_peso = 9.56
        return self._fator_peso

    @property
    def fator_altura(self):
        if self._fator_altura == None:
            if self._sexo == 1:
                self._fator_altura = 5
            else:
                self._fator_altura = 1.85
        return self._fator_altura

    @property
    def fator_idade(self):
        if self._fator_idade == None:
            if self._sexo == 1:
                self._fator_idade = 6.76
            else:
                self._fator_idade = 4.68
        return self._fator_idade

    @property
    def fator_atividade_fisica(self):
        if self._fator_atividade_fisica == None:
            if self._atividade_fisica == 1:
                self._fator_atividade_fisica = 1.2
            elif self._atividade_fisica == 2:
                self._fator_atividade_fisica = 1.375
            elif self._atividade_fisica == 3:
                self._fator_atividade_fisica = 1.55
            elif self._atividade_fisica == 4:
                self._fator_atividade_fisica = 1.725
            elif self._atividade_fisica == 5:
                self._fator_atividade_fisica = 1.9
        return self._fator_atividade_fisica