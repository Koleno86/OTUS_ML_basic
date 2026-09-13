"""
Доработайте класс `Vehicle`
"""
from homework_05.exceptions import NotEnoughFuel, LowFuelError
from dataclasses import dataclass
from abc import ABC

class Vehicle(ABC):
    def __init__(self, weight: int, fuel: float, fuel_consumption: float) -> None:
        self.weight: int = weight
        self.started: bool = False
        self.fuel: float = fuel
        self.fuel_consumption: float = fuel_consumption
        self.odo: float = 0.0

    def __str__(self) -> str:
        return f"""
        Weight: {self.weight}
        Fuel: {self.fuel:.2f}
        Fuel consumption: {self.fuel_consumption:.1f}
        ODO: {self.odo:.2f}
        """

    def start(self) -> bool:
        if not self.started:
           if self.fuel < 0:
               raise LowFuelError
           self.started = True

        return self.started

    def move(self, distance: float) -> None:
        distance_comsumption: float = ( distance * self.fuel_consumption ) / 100 

        if self.fuel < distance_comsumption:
            raise NotEnoughFuel

        self.fuel -= distance_comsumption
        self.odo += distance