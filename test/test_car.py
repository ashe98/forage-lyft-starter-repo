import unittest
from datetime import datetime
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

from car_factory import CarFactory
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_calliope(
            today, last_service_date, current_mileage, last_service_mileage
        )
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_calliope(
            today, last_service_date, current_mileage, last_service_mileage
        )
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        today = datetime.today().date()

        car = CarFactory.create_calliope(
            today, last_service_date, current_mileage, last_service_mileage
        )
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        today = datetime.today().date()

        car = CarFactory.create_calliope(
            today, last_service_date, current_mileage, last_service_mileage
        )
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_glissade(
            today, last_service_date, current_mileage, last_service_mileage
        )
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_glissade(
            today, last_service_date, current_mileage, last_service_mileage
        )
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        today = datetime.today().date()
        car = CarFactory.create_glissade(
            today, last_service_date, current_mileage, last_service_mileage
        )
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        today = datetime.today().date()
        car = CarFactory.create_glissade(
            today, last_service_date, current_mileage, last_service_mileage
        )
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False

        car = CarFactory.create_palindrome(
            today, last_service_date, warning_light_is_on
        )
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = False

        car = CarFactory.create_palindrome(
            today, last_service_date, warning_light_is_on
        )
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True
        today = datetime.today().date()
        car = CarFactory.create_palindrome(
            today, last_service_date, warning_light_is_on
        )
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        today = datetime.today().date()
        car = CarFactory.create_palindrome(
            today, last_service_date, warning_light_is_on
        )
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_rorschach(
            today, last_service_date, current_mileage, last_service_mileage
        )
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_rorschach(
            today, last_service_date, current_mileage, last_service_mileage
        )
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        today = datetime.today().date()
        car = CarFactory.create_rorschach(
            today, last_service_date, current_mileage, last_service_mileage
        )
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        today = datetime.today().date()

        car = CarFactory.create_rorschach(
            today, last_service_date, current_mileage, last_service_mileage
        )
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_thovex(
            today, last_service_date, current_mileage, last_service_mileage
        )
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_thovex(
            today, last_service_date, current_mileage, last_service_mileage
        )
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        today = datetime.today().date()

        car = CarFactory.create_thovex(
            today, last_service_date, current_mileage, last_service_mileage
        )
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        today = datetime.today().date()

        car = CarFactory.create_thovex(
            today, last_service_date, current_mileage, last_service_mileage
        )
        self.assertFalse(car.needs_service())


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
