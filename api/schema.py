import datetime
import typing
import strawberry

from api.weather import WeatherPredictions


@strawberry.type
class DayWeather:
    year: int
    month: int
    day: int
    temperature: int


def map_day_weather(date: datetime.date, temperature: int) -> DayWeather:
    return DayWeather(
        year=date.year,
        month=date.month,
        day=date.day,
        temperature=temperature
    )


@strawberry.type
class Query:
    @strawberry.field
    def weather(self,
                city: typing.Annotated[
                    str, strawberry.argument(description="City to predict weather in.")] = 'London',
                days_forward: typing.Annotated[
                    int, strawberry.argument(description="Number of days to predict the weather, starting today.")] = 5
                ) -> \
            typing.List[DayWeather]:
        weather_predictions = WeatherPredictions(city, days_forward)

        predictions = [map_day_weather(date, temperature) for (date, temperature) in
                       weather_predictions.get_predictions()]

        return predictions
