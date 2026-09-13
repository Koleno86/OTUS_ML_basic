from homework_05.car import Car
from homework_05.plane import Plane
from homework_05.engine import Engine
from homework_05.exceptions import LowFuelError, NotEnoughFuel, CargoOverload

distances = [123, 435, 222, 14, 57, 344]

lada: Car = Car(1500, 70, 7.8)
lada.set_engine(Engine(1.6, 16))

try:
    lada.start()

    print("Start point", lada)
    for distance in distances:
        print("Next point in", distance, "km") 
        lada.move(distance)
        print("The point is reached!", lada)
except LowFuelError:
    print("You have to fill your tank")
except NotEnoughFuel:
    print("The point is unreachable. Not enough fuel for the ride")

print()
print("-" * 40)
print()

cargos = [4.5, 13.2, 0.01, 2, 5]

an576: Plane = Plane(20000, 1400, 112, 20) 

try:
    print("A plane arrived for loading", an576)
    for cargo in cargos:
        print()
        print(f"Trying to load {cargo} T cargo")
        an576.load_cargo(cargo)
        print(an576)
except CargoOverload:
    print("Unable to load a cargo. The plain is overloaded")

print()
print(f"Unloading of {an576.remove_all_cargo()} T cargo is completed")
