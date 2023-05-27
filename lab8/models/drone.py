"""
A class that inherits from an abstract class
"""
from models.aerial_vehicle import AerialVehicle


class Drone(AerialVehicle):
    """Class representing a Drone."""

    def __init__(self, manufacturer="", max_speed=0, engine_type=0, battery_capacity_in_mah=0,
                 charge_consuming_per_minute_in_percentage=0,
                 max_weapon_weight_in_grams=0, max_cargo_weight_in_grams=0):
        """Initialize the Drone class."""

        super().__init__(manufacturer, max_speed, engine_type)
        self.battery_capacity_in_mah = battery_capacity_in_mah
        self.charge_consuming_per_minute_in_percentage = charge_consuming_per_minute_in_percentage
        self.max_weapon_weight_in_grams = max_weapon_weight_in_grams
        self.max_cargo_weight_in_grams = max_cargo_weight_in_grams

    MAX_BATTERY_CAPACITY_IN_PERCENTAGE = 100

    def get_max_flying_distance(self):
        """Calculate the maximum flying distance of the Drone.

        Returns:
            int: The maximum flying distance.
        """
        return int(self.max_speed * (self.MAX_BATTERY_CAPACITY_IN_PERCENTAGE
                                     / self.charge_consuming_per_minute_in_percentage))

    def get_max_delivery_weight(self):
        """Get the maximum delivery weight of the Drone.

        Returns:
            int: The maximum delivery weight.
        """
        return self.max_cargo_weight_in_grams + self.max_weapon_weight_in_grams

    def __str__(self):
        """Return a string representation of the Drone.

        Returns:
            str: String representation of the Drone.
        """
        return f"Drone(manufacturer={self.manufacturer}, max_speed={self.max_speed}," \
               f" engine_type={self.engine_type}, battery_capacity_in_mAh={self.battery_capacity_in_mah}, " \
               f"charge_consuming_per_minute_in_percentage={self.charge_consuming_per_minute_in_percentage}, " \
               f"max_weapon_weight_in_grams={self.max_weapon_weight_in_grams}, " \
               f"max_cargo_weight_in_grams={self.max_cargo_weight_in_grams})"
