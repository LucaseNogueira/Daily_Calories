from src.domain.ports.servicos.bo.bo_pessoa_adapter_port import BoPessoaAdapterPort

class BoPessoaAdapter(BoPessoaAdapterPort):
    
    def fator_peso(self, sexo:int)->float:
        '''Retorna o fator que será multiplicado com o peso da pessoa para integrar no calculo do gasto energético basal. Este fator é estimado de acordo com o sexo da pessoa.

        Example:
        - Se pessoa.sexo for igual a Masculino então retorne 13.75
        - Se pessoa.sexo for igual a Feminino então retorne 9.56

        Outputs:
        - Fator peso
        '''
        if sexo == 1:
            fator_peso = 13.75
        else:
            fator_peso = 9.56
        return fator_peso

    def fator_altura(self, sexo:int)->float:
        '''Retorna o fator que será multiplicado com a altura da pessoa para integrar no calculo do gasto energético basal. Este fator é estimado de acordo com o sexo da pessoa.

        Example:
        - Se pessoa.sexo for igual a Masculino então retorne 5
        - Se pessoa.sexo for igual a Feminino então retorne 1.85

        Outputs:
        - Fator altura
        '''
        if sexo == 1:
            fator_altura = 5
        else:
            fator_altura = 1.85
        return fator_altura

    def fator_idade(self, sexo:int)->float:
        '''Retorna o fator que será multiplicado com a idade da pessoa para integrar no calculo do gasto energético basal. Este fator é estimado de acordo com o sexo da pessoa.

        Example:
        - Se pessoa.sexo for igual a Masculino então retorne 6.76
        - Se pessoa.sexo for igual a Feminino então retorne 4.68

        Outputs:
        - Fator peso
        '''
        if sexo == 1:
            fator_idade = 6.76
        else:
            fator_idade = 4.68
        return fator_idade

    def fator_atividade_fisica(self, atividade_fisica:int)->float:
        '''Retorna o fator que será multiplicado com o gasto energético basal da pessoa no calculo de calórias diárias. Este fator é estimado de acordo com a pratica de atividade fisica da pessoa.

        Example:
        - Se pessoa.atividade_fisica for igual a Sedentário então retorne 1.2
        - Se pessoa.atividade_fisica for igual a Levemente Ativo então retorne 1.375

        Outputs:
        - Fator atividade fisica
        '''
        if atividade_fisica == 1:
            fator_atividade_fisica = 1.2
        elif atividade_fisica == 2:
            fator_atividade_fisica = 1.375
        elif atividade_fisica == 3:
            fator_atividade_fisica = 1.55
        elif atividade_fisica == 4:
            fator_atividade_fisica = 1.725
        elif atividade_fisica == 5:
            fator_atividade_fisica = 1.9
        return fator_atividade_fisica