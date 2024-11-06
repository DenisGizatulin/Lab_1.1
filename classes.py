class Vehicle: # Создано базовый класс транспорта
    def __init__(self, name, capacity) -> None:
        self.name = name
        self.capacity = capacity

    def start(self) -> None:
        print(f"{self._name} Двигается.")

    def info(self) -> None:
        print(f"Название: {self._name}, Вместимость: {self.capacity} единиц")


class Car(Vehicle): # Далее идут наследованные от Vehicle классы
    def activate(self) -> None:
        print(f"{self._name} едет по дороге")


class Truck(Vehicle):
    def activate(self) -> None:
        print(f"{self._name} едет по дороге")


class Bus(Vehicle):
    def activate(self) -> None:
        print(f"{self._name} едет по автобусной полосе")


class Bicycle(Vehicle):
    def activate(self) -> None:
        print(f"{self._name} едет по тротуару")


class Motorcycle(Vehicle):
    def activate(self) -> None:
        print(f"{self._name} едет по дороге")


class MetroTrain(Vehicle):
    def activate(self) -> None:
        print(f"{self._name} едет под землёй")


class Train(Vehicle):
    def activate(self) -> None:
        print(f"{self._name} едет по ЖД")


class Ship(Vehicle):
    def activate(self) -> None:
        print(f"{self._name} плывёт по морю")


class Plane(Vehicle):
    def activate(self) -> None:
        print(f"{self._name} летит по небу")