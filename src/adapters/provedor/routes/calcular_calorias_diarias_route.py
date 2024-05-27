from src.adapters.provedor.requests.calcular_calorias_diarias_request import CalcularCaloriasDiariasRequest
from src.adapters.servicos.bo.bo_pessoa_adapter import BoPessoaAdapter
from src.adapters.servicos.controllers.calcula_calorias_diarias_adapter import CalculaCaloriasDiariasAdapter
from src.adapters.servicos.controllers.calcula_geb_adapter import CalculaGEBAdapter
from src.domain.use_cases.calcular_calorias_diarias_use_case import CalcularCaloriasDiariasUseCase
from src.adapters.provedor.responses.calcular_calorias_diarias_response import CalcularCaloriasDiariasResponse
from src.adapters.provedor.responses.message import MessageSucesso, MessageInternaServerlError
from src.utils.log_request import LogRequest

class CalcularCaloriasDiariasRoute:

    @classmethod
    def get_gasto_calorico_diario(self,sexo: int, peso: float, altura: float, idade: int, atividade_fisica: int):
        try:
            request = CalcularCaloriasDiariasRequest(sexo,peso,altura,idade,atividade_fisica)
            calcular_use_case = CalcularCaloriasDiariasUseCase(CalculaGEBAdapter(BoPessoaAdapter()), CalculaCaloriasDiariasAdapter(BoPessoaAdapter()))
            calorias_diarias_response = CalcularCaloriasDiariasResponse(calcular_use_case.execute(request.to_domain()))
            message = MessageSucesso('Requisição realizada com sucesso!')
            message.set_body(calorias_diarias_response.to_dict)
            return message.to_dict
        except Exception:
            message = MessageInternaServerlError('Ocorreu uma falha interna no servidor')
            log = LogRequest(message)
            log.cadastrar
            return message.to_dict