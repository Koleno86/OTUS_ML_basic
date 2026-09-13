"""
Создайте класс `Car`, наследник `Vehicle`
"""

from homework_05.base import Vehicle
from homework_05.engine import Engine

class Car(Vehicle):
    def __init__(self, weight: int, fuel: float, fuel_consumption: float) -> None:
        super().__init__(weight, fuel, fuel_consumption)
        self.engine: Engine = None

    def __str__(self) -> str:
        return super().__str__() if not self.engine else super().__str__() + \
            f"""Engine volume {self.engine.volume}, {self.engine.pistons} pitons"""

    def set_engine(self, engine: Engine) -> None:
        self.engine = engine