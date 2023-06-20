"""
A class that inherits from an abstract class
"""
from models.aerial_vehicle import AerialVehicle


class PassengerPlane(AerialVehicle):
    """Class representing a Passenger Plane that inherits from the AerialVehicle class."""

    def get_max_delivery_weight(self):
        """Get the maximum delivery weight the plane can carry.

        Returns:
            float: The maximum delivery weight based on fuel capacity and fuel consumption rate.
        """

        return (self.fuel_capacity / self.fuel_consumption_in_liters_per_hour) * self.max_speed

    def get_max_flying_distance(self):
        """Get the maximum flying distance of the plane.

        Returns:
            float: The maximum flying distance based on the maximum cargo weight and maximum passengers weight.
        """

        return self.max_passengers_weight + self.max_cargo_weight

    def __init__(self, task_variations=None, manufacturer="", max_speed=0, engine_type=0,
                 max_cargo_weight=0, max_passengers_weight=0,
                 fuel_capacity=0, fuel_consumption_in_liters_per_hour=0, current_fuel=0):
        """Initialize the PassengerPlane class."""

        super().__init__(task_variations, manufacturer, max_speed, engine_type)
        if task_variations is None:
            task_variations = {}
        self.max_cargo_weight = max_cargo_weight
        self.max_passengers_weight = max_passengers_weight
        self.fuel_capacity = fuel_capacity
        self.fuel_consumption_in_liters_per_hour = fuel_consumption_in_liters_per_hour
        self.current_fuel = current_fuel

    def fuel_dumping(self, distance_to_base):
        """Check if fuel dumping is required based on the distance to the base.

        Args:
            distance_to_base (float): The distance to the base.

        Returns:
            bool: True if fuel dumping is required, False otherwise.
        """

        fuel_required = (distance_to_base / self.max_speed) * self.fuel_consumption_in_liters_per_hour
        return bool(fuel_required > self.current_fuel)

    def remaining_distance(self):
        """Calculate the remaining distance the plane can fly based on the current fuel level.

        Returns:
            float: The remaining distance the plane can fly.
        """

        return (self.current_fuel / self.fuel_consumption_in_liters_per_hour) * self.max_speed

    def __str__(self):
        """Return a string representation of the PassengerPlane object.

        Returns:
            str: String representation of the PassengerPlane object."""

        return f"Passenger Plane(task_variations = {self.task_variations}, " \
               f"manufacturer={self.manufacturer}, max_speed={self.max_speed}," \
               f" engine_type={self.engine_type}, max_cargo_weight={self.max_cargo_weight}, " \
               f"max_passengers_weight={self.max_passengers_weight}, fuel_capacity={self.fuel_capacity}, " \
               f"fuel_consumption_in_liters_per_hour={self.fuel_consumption_in_liters_per_hour}, " \
               f"current_fuel={self.current_fuel})"
