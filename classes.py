class Vehicle:  # Создан базовый класс транспорта
    def __init__(self, name, capacity) -> None:
        self.name = name
        self.capacity = capacity

    def start(self) -> None:
        print(f"{self.name} Двигается.")

    def info(self) -> str:
        return f"Название: {self.name}, Вместимость: {self.capacity} единиц"

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "name": self.name,
            "capacity": self.capacity,
        }


class Car(Vehicle):  # Далее идут наследованные от Vehicle классы
    def activate(self) -> None:
        print(f"{self.name} едет по дороге")

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "name": self.name,
            "capacity": self.capacity,
        }


class Truck(Vehicle):
    def activate(self) -> None:
        print(f"{self.name} едет по дороге")

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "name": self.name,
            "capacity": self.capacity,
        }


class Bus(Vehicle):
    def activate(self) -> None:
        print(f"{self.name} едет по автобусной полосе")

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "name": self.name,
            "capacity": self.capacity,
        }


class Bicycle(Vehicle):
    def activate(self) -> None:
        print(f"{self.name} едет по тротуару")

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "name": self.name,
            "capacity": self.capacity,
        }


class Motorcycle(Vehicle):
    def activate(self) -> None:
        print(f"{self.name} едет по дороге")

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "name": self.name,
            "capacity": self.capacity,
        }


class MetroTrain(Vehicle):
    def activate(self) -> None:
        print(f"{self.name} едет под землёй")

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "name": self.name,
            "capacity": self.capacity,
        }


class Train(Vehicle):
    def activate(self) -> None:
        print(f"{self.name} едет по ЖД")

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "name": self.name,
            "capacity": self.capacity,
        }


class Ship(Vehicle):
    def activate(self) -> None:
        print(f"{self.name} плывёт по морю")

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "name": self.name,
            "capacity": self.capacity,
        }


class Plane(Vehicle):
    def activate(self) -> None:
        print(f"{self.name} летит по небу")

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "name": self.name,
            "capacity": self.capacity,
        }
