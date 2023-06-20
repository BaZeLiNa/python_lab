"""
Class manager to create objects and validate methods
"""
from functools import wraps
from models.helicopter import Helicopter
from models.drone import Drone
from models.fighter import Fighter
from models.passenger_plane import PassengerPlane
from models.engine_type import EngineType
from managers.aerial_vehicle_sm import AerialVehicleManagerSM


def decorator_number_four(function):
    """ Docstring"""
    @wraps(function)
    def wrapper(*args, **kwargs):
        """
        A decorator that logs the input and output parameters of a function.

        Args:
            *args: Positional arguments passed to the function.
            **kwargs: Keyword arguments passed to the function.

        Returns:
            The result of the decorated function.
        """
        print("")
        print(f"Input parameters for {function.__name__}:")
        print("Positional arguments:", args)
        print("Keyword arguments:", kwargs)

        result = function(*args, **kwargs)

        print(f"Output parameters for: {function.__name__}")
        print("Result:", result)
        print("")
        return result

    return wrapper


def decorator_number_eleven(function):
    """Docstring"""
    @wraps(function)
    def wrapper(*args, **kwargs):
        """
        A decorator that prints the length of the iterable object returned by a function.

        Args:
            *args: Positional arguments passed to the function.
            **kwargs: Keyword arguments passed to the function.

        Returns:
            The result of the decorated function.
        """
        result = function(*args, **kwargs)
        try:
            length = len(result)
        except TypeError:
            length = 1
        print("")
        print(f"The length of the iterable object: {length}")
        print("")
        return result

    return wrapper


class AerialVehicleManagerRM:
    """Class for managing aerial vehicles.

    Attributes:
        aerial_vehicles (list): List of aerial vehicles.
    """

    def __init__(self):
        """Initialize the AerialVehicleManager class."""
        self.aerial_vehicles = []

    def add_aerial_vehicle(self, new_aerial_vehicle):
        """Add an aerial vehicle to the manager.

        Args:
            new_aerial_vehicle (AerialVehicle): The aerial vehicle to be added.
        """
        self.aerial_vehicles.append(new_aerial_vehicle)

    def find_speed_greater_than(self, speed):
        """Find aerial vehicles with speed greater than the given speed.

        Args:
            speed (int): The speed threshold.

        Returns:
            list: List of aerial vehicles with speed greater than the given speed.
        """
        return filter(lambda func_vehicle: getattr(func_vehicle, 'max_speed') > speed, self.aerial_vehicles)

    def find_by_engine_type(self, engine_type):
        """Find aerial vehicles with the specified engine type.

        Args:
            engine_type (EngineType): The engine type to search for.

        Returns:
            list: List of aerial vehicles with the specified engine type.
        """
        return filter(lambda func_vehicle: getattr(func_vehicle, 'engine_type') == engine_type, self.aerial_vehicles)

    def __len__(self):
        return len(self.aerial_vehicles)

    def __getitem__(self, index):
        return self.aerial_vehicles[index]

    def __iter__(self):
        return iter(self.aerial_vehicles)

    def func_with_comprehension(self):
        """
        Return a list of maximum flying distances using a list comprehension.

        Returns:
            list: A list of maximum flying distances.
        """
        return [getattr(element, "get_max_flying_distance") for element in self.aerial_vehicles]

    def func_with_enumerate(self):
        """
        Print the index and corresponding element of each aerial vehicle.

        """
        for index, element1 in enumerate(self.aerial_vehicles):
            print(f" {index} - this is the index of this element: {element1}")

    def func_with_zip(self):
        """
        Print the maximum flying distance and corresponding aerial vehicle using zip.

        """
        list_max_flying_distance = self.func_with_comprehension()
        for max_flying_distance_element, aerial_vehicles_element in zip(list_max_flying_distance,
                                                                        self.aerial_vehicles):
            print(f"Max flying distance {max_flying_distance_element} of this: {aerial_vehicles_element}")

    @decorator_number_four
    @decorator_number_eleven
    def func_with_all_any(self, speed):
        """
        Check if all or any aerial vehicles have a maximum speed greater than the specified speed.

        Args:
            speed (float): The speed threshold.

        Returns:
            dict: A dictionary with keys "all" and "any" indicating the results of the checks.
        """
        print("/n/n")
        print(f"Function name: {self.func_with_all_any.__name__}")
        print(f"Function docstring {self.func_with_all_any.__doc__}")
        return {
            "all": all(getattr(element, "max_speed") > speed for element in self.aerial_vehicles),
            "any": any(getattr(element, "max_speed") > speed for element in self.aerial_vehicles)
        }


if __name__ == "__main__":
    aerial_vehicle_manager = AerialVehicleManagerRM()
    aerial_vehicle_manager.add_aerial_vehicle(
        Helicopter({"crew transport", "weapons transport", "combat"}, "Boeing",
                   120, EngineType.PISTON, "CH-47", 0, 3000, 600, 560, 35, 600, 500))
    aerial_vehicle_manager.add_aerial_vehicle(
        Helicopter({"reconnaissance", "combat"}, "Bell",
                   150, EngineType.PISTON, "UH-1", 1200, 2200, 500, 300, 40, 400, 300))
    aerial_vehicle_manager.add_aerial_vehicle(Drone({"reconnaissance", "drop grenade"},
                                                    "DJI", 50, EngineType.ELECTRIC, 4, 100, 200))
    aerial_vehicle_manager.add_aerial_vehicle(Drone({"reconnaissance"}, "DJI 2", 30, EngineType.ELECTRIC, 2, 0, 500))
    aerial_vehicle_manager.add_aerial_vehicle(Fighter({"reconnaissance, air combat, accompaniment"}, "F-14", 1300,
                                                      EngineType.GAS_TURBINE, 600, 400, 150, 350))
    aerial_vehicle_manager.add_aerial_vehicle(Fighter({"reconnaissance", "air combat", "bombing of the reds"},
                                                      "F-16", 1500, EngineType.GAS_TURBINE, 700, 600, 140, 600))
    aerial_vehicle_manager.add_aerial_vehicle(
        PassengerPlane({"crew transport", "weapons transport"}, "Boeing 747",
                       800, EngineType.GAS_TURBINE, 25000, 10000, 40000, 400, 25000))
    aerial_vehicle_manager.add_aerial_vehicle(
        PassengerPlane({"transport goods"}, "Boeing 737", 700, EngineType.GAS_TURBINE, 20000, 15000, 30000, 500, 28000))

    for aerial_vehicle in aerial_vehicle_manager.aerial_vehicles:
        print(aerial_vehicle)

    print("\n\nAerial vehicles faster than 200 km/h:")
    vehicles_speed_greater_than = aerial_vehicle_manager.find_speed_greater_than(200)
    for vehicle in vehicles_speed_greater_than:
        print(vehicle)
    print("")
    aerial_vehicle_manager.func_with_enumerate()
    print("")
    aerial_vehicle_manager.func_with_zip()
    for vehicle in aerial_vehicle_manager.aerial_vehicles:
        print(vehicle.func_with_dict(int))
    print("")
    print("")
    print("")
    print("")
    print(aerial_vehicle_manager.func_with_all_any(200))
    #print(aerial_vehicle_manager.func_with_all_any(200).__name__())
    #print(aerial_vehicle_manager.func_with_all_any(200).__doc__())
    test_manager = AerialVehicleManagerSM(aerial_vehicle_manager)
    for element in test_manager:
        print(0)
    print("")
    for element in test_manager:
        print(1)
    print("")
    for element in test_manager:
        print(2)
    exception_test_object = Helicopter({"crew transport", "weapons transport", "combat"}, "Boeing", 120,
                                       EngineType.PISTON, "CH-47", 0, 3000, 600, 560, 35, 600, 500)
    print("\n\n\n")

    exception_test_object.ascend(3100)
    exception_test_object.descend(3100)
    exception_test_object.refuel(50)

