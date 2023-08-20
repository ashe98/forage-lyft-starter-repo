from datetime import datetime
import unittest

from tire.octoprime_tire import OctoprimeTire


class TestOctoprimeTire(unittest.TestCase):
    def test_should_be_serviced(self):
        tire = OctoprimeTire([1, 1, 1, 0])
        self.assertTrue(tire.needs_service())

    def test_should_not_be_serviced(self):
        tire = OctoprimeTire([0.2, 0.3, 0, 0])
        self.assertFalse(tire.needs_service())
