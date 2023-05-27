"""
Class manager to create objects and validate methods
"""

from models.helicopter import Helicopter
from models.drone import Drone
from models.fighter import Fighter
from models.passenger_plane import PassengerPlane
from models.engine_type import EngineType


class AerialVehicleManager:
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
        return


aerial_vehicle_manager = AerialVehicleManager()
aerial_vehicle_manager.add_aerial_vehicle(
    Helicopter("Boeing", 120, EngineType.PISTON, "CH-47", 0, 3000, 600, 560, 35, 600, 500))
aerial_vehicle_manager.add_aerial_vehicle(
    Helicopter("Bell", 150, EngineType.PISTON, "UH-1", 1200, 2200, 500, 300, 40, 400, 300))
aerial_vehicle_manager.add_aerial_vehicle(Drone("DJI", 50, EngineType.ELECTRIC, 4, 100, 200))
aerial_vehicle_manager.add_aerial_vehicle(Drone("DJI 2", 30, EngineType.ELECTRIC, 2, 0, 500))
aerial_vehicle_manager.add_aerial_vehicle(Fighter("F-14", 1300, EngineType.GAS_TURBINE, 600, 400, 150, 350))
aerial_vehicle_manager.add_aerial_vehicle(Fighter("F-16", 1500, EngineType.GAS_TURBINE, 700, 600, 140, 600))
aerial_vehicle_manager.add_aerial_vehicle(
    PassengerPlane("Boeing 747", 800, EngineType.GAS_TURBINE, 25000, 10000, 40000, 400, 25000))
aerial_vehicle_manager.add_aerial_vehicle(
    PassengerPlane("Boeing 737", 700, EngineType.GAS_TURBINE, 20000, 15000, 30000, 500, 28000))

for aerial_vehicle in aerial_vehicle_manager.aerial_vehicles:
    print(aerial_vehicle)

print("\n\nAerial vehicles faster than 200 km/h:")
vehicles_speed_greater_than = aerial_vehicle_manager.find_speed_greater_than(200)
for vehicle in vehicles_speed_greater_than:
    print(vehicle)
