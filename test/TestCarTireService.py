import unittest
from datetime import datetime
from car import Car
from engine.capulet_engine import CapuletEngine
from battery.spindler_battery import SpindlerBattery

class TestCarTireService(unittest.TestCase):
    def test_carrigan_tire_service(self):
        # Create a car with Carrigan tires that need servicing
        car = Car(CapuletEngine(datetime.today().date(), 30000, 0), 
                  SpindlerBattery(datetime.today().date(), datetime.today().date()), 
                  "Carrigan", [0.8, 0.9, 0.85, 0.7])
        self.assertTrue(car.needs_service())

    def test_octoprime_tire_service(self):
        # Create a car with Octoprime tires that need servicing
        car = Car(CapuletEngine(datetime.today().date(), 30000, 0), 
                  SpindlerBattery(datetime.today().date(), datetime.today().date()), 
                  "Octoprime", [0.8, 0.9, 0.85, 0.7])
        self.assertTrue(car.needs_service())

    def test_no_tire_service_needed(self):
        # Create a car with no tire servicing needed
        car = Car(CapuletEngine(datetime.today().date(), 30000, 0), 
                  SpindlerBattery(datetime.today().date(), datetime.today().date()), 
                  "Carrigan", [0.8, 0.7, 0.75, 0.7])
        self.assertFalse(car.needs_service())

if __name__ == '__main__':
    unittest.main()
