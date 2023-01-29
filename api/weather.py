import typing
import random
from datetime import datetime, timedelta


class WeatherPredictions:
    MIN_TEMP = -20
    MAX_TEMP = 30

    def __init__(self, city: str, days_forward: int):
        self.city = city
        self.days_forward = days_forward

    def get_predictions(self) -> typing.List[typing.Tuple[datetime.date, int]]:
        result = []
        date = datetime.today()
        random.seed(self.city)
        for i in range(self.days_forward):
            temperature = random.randint(self.MIN_TEMP, self.MAX_TEMP)
            result.append((date, temperature))
            date += timedelta(days=1)

        return result
