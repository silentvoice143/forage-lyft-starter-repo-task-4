import unittest
from datetime import datetime
from batterys.spindlerbattery import SpindlerBattery

class Spindlertest:
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        battery=SpindlerBattery(last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        battery=SpindlerBattery(last_service_date)
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()