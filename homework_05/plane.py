"""
Создайте класс `Plane`, наследник `Vehicle`
"""

from homework_05.exceptions import CargoOverload
from homework_05.base import Vehicle 

class Plane(Vehicle):
    def __init__(self, weight: int, fuel: float, fuel_consumption: float, max_cargo: float) -> None:
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo: float = max_cargo
        self.cargo: float = 0.0

    def __str__(self) -> str:
        return super().__str__() + \
            f"""Load: {self.cargo} per {self.max_cargo}"""

    def load_cargo(self, cargo: float) -> None:
        if self.cargo + cargo > self.max_cargo:
            raise CargoOverload

        self.cargo += cargo

    def remove_all_cargo(self) -> float:
        prev_cargo: float = self.cargo
        self.cargo = 0.0
        return prev_cargo