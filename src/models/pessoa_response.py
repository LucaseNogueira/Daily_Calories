from src.models.interfaces.response_interface import ResponseInterface

class PessoaResponse(ResponseInterface):

    def __init__(self, daily_calories:float):
        self.daily_calories = daily_calories

    @property
    def to_dict(self) -> dict:
        return {
            'daily_calories': self.daily_calories
        }