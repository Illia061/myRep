class Vehicle:
    """
    Базовий клас Vehicle для транспортних засобів.
    """

    def __init__(self, make, model):
        """
        Ініціалізація нового транспортного засобу.

        :param make: Марка транспортного засобу.
        :type make: str
        :param model: Модель транспортного засобу.
        :type model: str
        """
        self.make = make
        self.model = model

    def honk(self):
        """Функція honk виводить гудок транспортного засобу."""
        print("Beep!")


class LandVehicle(Vehicle):
    """
    Підклас LandVehicle представляє наземні транспортні засоби.
    Підклас LandVehicle наслдіує базовий клас Vehicle
    """
    def drive(self):
        """Функція drive виводить повідомлення про рух по суші."""
        print("Їдемо по суші")


class WaterVehicle(Vehicle):
    """
    Підклас WaterVehicle представляє водні транспортні засоби.
    Підклас WaterVehicle наслдіує базовий клас Vehicle
    """

    def sail(self):
        """Функція sail виводить повідомлення про плавання по воді."""
        print("Пливемо по воді")


class Car(LandVehicle):
    """
    Підклас Car представляє автомобілі.
    Підклас Car наслідує підклас клас LandVehicle
    """

    def open_trunk(self):
        """Функція open_trunk виводить повідомлення, що багажник відкрито."""
        print("Багажник відкрито")


class Truck(LandVehicle):
    """
    Підклас Truck представляє вантажівки.
    Підклас Truck наслідує підклас клас LandVehicle
    """

    def load_cargo(self):
        """Функція load_cargo повідомлення, що завантажено вантаж."""
        print("Вантаж завантажено")


class Boat(WaterVehicle):
    """
    Підклас Boat представляє човни.
    Підклас Truck наслідує підклас клас WaterVehicle.
    """

    def anchor(self):
        """Функція anchor виводить повідомлення, що човен на якорі."""
        print("Човен на якорі")


class Ship(WaterVehicle):
    """
    Підклас Ship представляє кораблі.
    Підклас Ship наслідує підклас клас WaterVehicle.
    """

    def sound_horn(self):
        """Функція sound_horn виводить повідомлення, що гудок корабля."""
        print("Гудок корабля")

    # Приклад використання класів
car = Car("Toyota", "Camry")
car.honk()
car.drive()
car.open_trunk()

truck = Truck("Volvo", "VNL")
truck.honk()
truck.drive()
truck.load_cargo()

boat = Boat("Yamaha", "242X")
boat.honk()
boat.sail()
boat.anchor()

ship = Ship("Royal Caribbean", "Freedom of the Seas")
ship.honk()
ship.sail()
ship.sound_horn()