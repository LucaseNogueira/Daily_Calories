
class Pessoa:

    def __init__(self, sexo:int, peso:float, altura:float, idade:int, atividade_fisica:int):
        self._sexo = sexo
        self._peso = peso
        self._altura = altura
        self._idade = idade
        self._atividade_fisica = atividade_fisica

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
    def atividade_fisica(self):
        return self._atividade_fisica