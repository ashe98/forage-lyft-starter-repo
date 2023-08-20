from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        res = False
        for component, value in self.__dict__.items():
            res = res or component.needs_service()
        return res
