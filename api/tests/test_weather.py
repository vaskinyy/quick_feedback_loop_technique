from unittest import TestCase

from api.weather import WeatherPredictions


class ApiTests(TestCase):
    def test_return_given_days_forward(self):
        weather_predictions = WeatherPredictions("London", 5)
        predictions = weather_predictions.get_predictions()
        self.assertEqual(len(predictions), 5)

    def test_predictions_within_given_range(self):
        weather_predictions = WeatherPredictions("London", 5)
        predictions = weather_predictions.get_predictions()
        for _, temperature in predictions:
            self.assertGreaterEqual(temperature, WeatherPredictions.MIN_TEMP)
            self.assertLessEqual(temperature, WeatherPredictions.MAX_TEMP)
