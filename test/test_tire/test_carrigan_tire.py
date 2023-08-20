from datetime import datetime
import unittest

from tire.carrigan_tire import CarriganTire


class TestCarriganTire(unittest.TestCase):
    def test_should_be_serviced(self):
        tire = CarriganTire([1, 0, 0, 0])
        self.assertTrue(tire.needs_service())

    def test_should_not_be_serviced(self):
        tire = CarriganTire([0.2, 0, 0, 0])
        self.assertFalse(tire.needs_service())
