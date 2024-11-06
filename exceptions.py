class InvalidVehicleTypeException(Exception):
    def __init__(self, vehicle_type):
        super().__init__(f"Неверный тип транспорта: {vehicle_type}. ")


class InvalidFileTypeException(Exception):
    def __init__(self, file_type):
        super().__init__(f"Неверный тип файла: {file_type}. Допустимые типы: json, xml.")