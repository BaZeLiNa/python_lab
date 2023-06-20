"""
A class Helicopter
"""


class Helicopter:
    """Class representing a Helicopter."""

    def __init__(self, model="", current_altitude=0, max_altitude=0,
                 fuel_capacity=0, current_fuel=0, fuel_consumption_in_liters_per_hour=0, max_weapon_weight=0,
                 max_cargo_weight=0):
        """Initialize the Helicopter class."""

        self.vehicle_id = 100
        self.model = model
        self.current_altitude = current_altitude
        self.max_altitude = max_altitude
        self.fuel_capacity = fuel_capacity
        self.current_fuel = current_fuel
        self.fuel_consumption_in_liters_per_hour = fuel_consumption_in_liters_per_hour
        self.max_weapon_weight = max_weapon_weight
        self.max_cargo_weight = max_cargo_weight

    def take_off(self):
        """Make the Helicopter take off by setting the current altitude to 100."""
        self.current_altitude = 100

    def ascend(self, altitude):
        """Ascend the Helicopter by a specified altitude.

        Args:
            altitude (int): The altitude to ascend.
        """
        if (self.current_altitude + altitude) <= self.max_altitude:
            self.current_altitude += altitude

    def descend(self, altitude):
        """Descend the Helicopter by a specified altitude.

        Args:
            altitude (int): The altitude to descend.
        """
        if self.current_altitude - altitude >= 0:
            self.current_altitude -= altitude
        else:
            self.current_altitude = 0

    def refuel(self, fuel):
        """Refuel the Helicopter with a specified amount of fuel.

        Args:
            fuel (int): The amount of fuel to refuel.
        """
        if self.current_fuel + fuel <= self.fuel_capacity:
            self.current_fuel += fuel
        else:
            self.current_fuel = self.fuel_capacity

    @classmethod
    def get_instance(cls):
        """Get an instance of the Helicopter class.

        Returns:
            Helicopter: An instance of the Helicopter class.
        """
        return cls()

    def __str__(self):
        """Return a string representation of the Helicopter.

        Returns:
            str: String representation of the Helicopter.
        """
        return f"Helicopter(vehicle_id={self.vehicle_id}, model={self.model}, " \
               f"current_altitude={self.current_altitude}, max_altitude={self.max_altitude}, " \
               f"fuel_capacity={self.fuel_capacity}, current_fuel={self.current_fuel})"
