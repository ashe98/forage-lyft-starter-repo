from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, wear: list[float]) -> None:
        self.wear = wear

    def needs_service(self):
        for w in self.wear:
            if w >= 0.9:
                return True
        return False
