from datetime import datetime
import unittest

from battery.nubbin_battery import NubbinBattery


class TestNubbinBattery(unittest.TestCase):
    def test_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 6)
        battery = NubbinBattery(current_date=today, last_service_date=last_service_date)
        self.assertTrue(battery.needs_service())

    def test_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        battery = NubbinBattery(current_date=today, last_service_date=last_service_date)
        self.assertFalse(battery.needs_service())
