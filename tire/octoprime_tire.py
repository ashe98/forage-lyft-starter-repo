from tire.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, wear: list[float]) -> None:
        self.wear = wear

    def needs_service(self):
        return sum(self.wear) >= 3
