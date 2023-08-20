from datetime import date
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class CarFactory:
    def create_calliope(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        engine = CapuletEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_date
        )
        battery = SpindlerBattery(
            last_service_date=last_service_date, current_date=current_date
        )
        car = Car(engine=engine, battery=battery)
        return car

    def create_glissade(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        engine = WilloughbyEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage
        )
        battery = SpindlerBattery(
            last_service_date=last_service_date, current_date=current_date
        )
        car = Car(engine=engine, battery=battery)
        return car

    def create_palindrome(
        current_date: date, last_service_date: date, warning_light_on: bool
    ) -> Car:
        engine = SternmanEngine(warning_light_is_on=warning_light_on)
        battery = SpindlerBattery(
            last_service_date=last_service_date, current_date=current_date
        )
        car = Car(engine=engine, battery=battery)
        return car

    def create_rorschach(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        engine = WilloughbyEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage
        )
        battery = NubbinBattery(
            last_service_date=last_service_date, current_date=current_date
        )
        car = Car(engine=engine, battery=battery)
        return car

    def create_thovex(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        engine = CapuletEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_date
        )
        battery = NubbinBattery(
            last_service_date=last_service_date, current_date=current_date
        )
        car = Car(engine=engine, battery=battery)
        return car
