from unittest import TestCase

from api.main import schema


class WeatherTests(TestCase):
    def test_returns_give_number_of_days(self):
        query = """
            query TestQuery($city: String!, $daysForward: Int!) {
                weather(city: $city, daysForward: $daysForward) {
                    year
                    month
                    day
                    temperature
                }
            }
        """

        result = schema.execute_sync(
            query,
            variable_values={"city": "London", "daysForward": 1},
        )
        self.assertEqual(result.errors, None)
        self.assertEqual(len(result.data['weather']), 1)
