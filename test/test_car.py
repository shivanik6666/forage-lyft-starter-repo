import unittest
from datetime import datetime
from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex

class CarTest(unittest.TestCase):
    def setUp(self):
        self.today = datetime.today().date()

    def test_calliope_battery_service(self):
        self._test_car_service(Calliope, 3, 0, 0, True)
        self._test_car_service(Calliope, 1, 0, 0, False)

    def test_calliope_engine_service(self):
        self._test_car_service(Calliope, 0, 30001, 0, True)
        self._test_car_service(Calliope, 0, 30000, 0, False)

    def test_glissade_battery_service(self):
        self._test_car_service(Glissade, 3, 0, 0, True)
        self._test_car_service(Glissade, 1, 0, 0, False)

    def test_glissade_engine_service(self):
        self._test_car_service(Glissade, 0, 60001, 0, True)
        self._test_car_service(Glissade, 0, 60000, 0, False)

    def test_palindrome_battery_service(self):
        self._test_car_service(Palindrome, 5, 0, 0, True)
        self._test_car_service(Palindrome, 3, 0, 0, False)

    def test_palindrome_engine_service(self):
        self._test_car_service(Palindrome, 0, 0, 0, True)
        self._test_car_service(Palindrome, 0, 0, 0, False)

    def test_rorschach_battery_service(self):
        self._test_car_service(Rorschach, 5, 0, 0, True)
        self._test_car_service(Rorschach, 3, 0, 0, False)

    def test_rorschach_engine_service(self):
        self._test_car_service(Rorschach, 0, 60001, 0, True)
        self._test_car_service(Rorschach, 0, 60000, 0, False)

    def test_thovex_battery_service(self):
        self._test_car_service(Thovex, 5, 0, 0, True)
        self._test_car_service(Thovex, 3, 0, 0, False)

    def test_thovex_engine_service(self):
        self._test_car_service(Thovex, 0, 30001, 0, True)
        self._test_car_service(Thovex, 0, 30000, 0, False)

    def _test_car_service(self, CarClass, years, mileage, last_service_mileage, should_service):
        last_service_date = self.today.replace(year=self.today.year - years)
        car = CarClass(last_service_date, mileage, last_service_mileage)
        self.assertEqual(car.needs_service(), should_service)

if __name__ == '__main__':
    unittest.main()
