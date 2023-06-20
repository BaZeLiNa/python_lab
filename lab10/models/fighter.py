"""
A class that inherits from an abstract class
"""
from exceptions import RefuelException
from decorators import logger
from models.aerial_vehicle import AerialVehicle


class Fighter(AerialVehicle):
    """Class representing a Fighter aircraft."""

    def get_max_flying_distance(self):
        """Calculate the maximum flying distance of the Fighter aircraft.

        Returns:
            int: The maximum flying distance.
        """
        return (self.fuel_capacity / self.fuel_consumption_in_liters_per_hour) * self.max_speed

    def get_max_delivery_weight(self):
        """Get the maximum delivery weight of the Fighter aircraft.

        Returns:
            int: The maximum delivery weight.
        """
        return self.max_weapon_weight

    def __init__(self, task_variations=None, manufacturer="", max_speed=0,
                 engine_type=0, max_weapon_weight=0, fuel_capacity=0,
                 fuel_consumption_in_liters_per_hour=0, current_fuel=0):
        """Initialize the Fighter class."""

        super().__init__(task_variations, manufacturer, max_speed, engine_type)
        if task_variations is None:
            task_variations = {}
        self.max_weapon_weight = max_weapon_weight
        self.fuel_capacity = fuel_capacity
        self.fuel_consumption_in_liters_per_hour = fuel_consumption_in_liters_per_hour
        self.current_fuel = current_fuel

    @logger(RefuelException, "console")
    def refuel(self, fuel):
        """Refuel the Fighter aircraft.

        Args:
            fuel (int): The amount of fuel to refuel.

        Returns:
            None
        """
        if (self.current_fuel + fuel) <= self.fuel_capacity:
            self.current_fuel += fuel
        else:
            self.current_fuel = self.fuel_capacity
            raise RefuelException("Too much")

    def fuel_dumping(self, distance_to_base):
        """Check if fuel dumping is required for the Fighter aircraft.

        Args:
            distance_to_base (int): The distance to the base.

        Returns:
            bool: True if fuel dumping is required, False otherwise.
        """
        fuel_required = (distance_to_base / self.max_speed) * self.fuel_consumption_in_liters_per_hour
        return bool(fuel_required > self.current_fuel)

    def __str__(self):
        """Return a string representation of the Fighter aircraft.

        Returns:
            str: String representation of the Fighter aircraft.
        """
        return f"Fighter(task_variations = {self.task_variations}, " \
               f"manufacturer={self.manufacturer}, max_speed={self.max_speed}," \
               f" engine_type={self.engine_type}, max_weapon_weight={self.max_weapon_weight}, " \
               f"fuel_capacity={self.fuel_capacity}, " \
               f"fuel_consumption_in_liters_per_hour={self.fuel_consumption_in_liters_per_hour}, " \
               f"current_fuel={self.current_fuel})"
