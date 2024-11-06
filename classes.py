class Vehicle: # Создан базовый класс транспорта
    def __init__(self, name, capacity) -> None:
        self.name = name
        self.capacity = capacity

    def start(self) -> None:
        print(f"{self._name} Двигается.")

    def info(self) -> None:
        print(f"Название: {self._name}, Вместимость: {self.capacity} единиц")

    @property # Добавлен декоратор для того, чтобы name стал свойством и была возможность установки значения этого поля сеттером
    def name(self) -> str:
        return self._name

    @name.setter # Сеттер для установки имени
    def name(self, name) -> None:
        if not isinstance(name, str):
            raise ValueError("Название должно быть строкой!")
        self._name = name

    @property # Аналогичный декоратор
    def capacity(self) -> int:
        return self._capacity

    @capacity.setter # Аналогичный сеттер
    def age(self, capacity) -> None:
        if not isinstance(capacity, int):
            raise ValueError("")
        self._capacity = capacity


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