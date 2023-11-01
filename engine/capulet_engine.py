from abc import ABC
from datetime import datetime

from car import Car

class CapuletEngine(Car, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date, current_mileage, last_service_mileage)

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 30000
