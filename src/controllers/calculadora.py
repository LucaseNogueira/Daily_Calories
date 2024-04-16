import sys
sys.path.append('.')

from src.models.pessoa import Pessoa

class Calculadora:
    
    def __init__(self, pessoa:Pessoa):
        self._fator_geb = 66.5 if pessoa.sexo == 1 else 665
        self._pessoa = pessoa

    def calcular_calorias_diarias(self) -> float:
        '''Calcula as calorias diárias da pessoa setada na calculadora

        Exemple:
        - homem: GEB * 66.5

        Outputs:
        - Calorias diárias calculada
        '''
        return self.calcular_geb() * self._pessoa.fator_atividade_fisica

    def calcular_geb(self) -> float:
        '''Calcula o gasto energético basal (GEB) conforme o peso, altura e idade da pessoa.

        Exemple:
        - homem: (13,75 x peso em quilos) + (5 x altura em centímetros) – (6,76 x idade em anos) + 66,5
        
        Outputs
        - Gasto energético basal de uma pessoa
        '''
        peso_calculado = self._pessoa.fator_peso * self._pessoa.peso
        altura_calculada = self._pessoa.fator_altura * self._pessoa.altura
        idade_calculada = self._pessoa.fator_idade * self._pessoa.idade
        return peso_calculado + altura_calculada - idade_calculada + self._fator_geb