import unittest
from datetime import datetime
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

from car_factory import CarFactory
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class TestCarFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.today = datetime.today().date()
        self.last_service_date = self.today.replace(year=self.today.year - 3)
        self.current_mileage = 0
        self.last_service_mileage = 0
        self.warning_light_is_on = False
        return super().setUp()

    def test_calliope_components(self):
        car = CarFactory.create_calliope(
            self.today,
            self.last_service_date,
            self.current_mileage,
            self.last_service_mileage,
        )
        self.assertIsInstance(car.engine, CapuletEngine)
        self.assertIsInstance(car.battery, SpindlerBattery)

    def test_glissade_components(self):
        car = CarFactory.create_glissade(
            self.today,
            self.last_service_date,
            self.current_mileage,
            self.last_service_mileage,
        )
        self.assertIsInstance(car.engine, WilloughbyEngine)
        self.assertIsInstance(car.battery, SpindlerBattery)

    def test_palindrome_components(self):
        car = CarFactory.create_palindrome(
            self.today, self.last_service_date, self.warning_light_is_on
        )
        self.assertIsInstance(car.engine, SternmanEngine)
        self.assertIsInstance(car.battery, SpindlerBattery)

    def test_thovex_components(self):
        car = CarFactory.create_thovex(
            self.today,
            self.last_service_date,
            self.current_mileage,
            self.last_service_mileage,
        )
        self.assertIsInstance(car.engine, CapuletEngine)
        self.assertIsInstance(car.battery, NubbinBattery)

    def test_rorschach_components(self):
        car = CarFactory.create_rorschach(
            self.today,
            self.last_service_date,
            self.current_mileage,
            self.last_service_mileage,
        )
        self.assertIsInstance(car.engine, WilloughbyEngine)
        self.assertIsInstance(car.battery, NubbinBattery)


if __name__ == "__main__":
    unittest.main()
