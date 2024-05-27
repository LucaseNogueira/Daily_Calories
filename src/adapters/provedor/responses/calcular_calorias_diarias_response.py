from src.adapters.interfaces.responses.response_interface import ResponseInterface

class CalcularCaloriasDiariasResponse(ResponseInterface):

    def __init__(self, daily_calories) -> None:
        self.daily_calories = daily_calories
        super().__init__()

    @property
    def to_dict(self) -> dict:
        return {
            'daily_calories': self.daily_calories
        }