"""
Abstract class
"""
from abc import ABC, abstractmethod


class AerialVehicle(ABC):
    """Abstract base class for aerial vehicles."""

    def __init__(self, manufacturer, max_speed, engine_type):
        """Initialize an aerial vehicle object."""

        self.manufacturer = manufacturer
        self.max_speed = max_speed
        self.engine_type = engine_type

    @abstractmethod
    def get_max_flying_distance(self):
        """Get the maximum flying distance of the aerial vehicle.

        Returns:
            int: The maximum flying distance.
        """

    @abstractmethod
    def get_max_delivery_weight(self):
        """Get the maximum delivery weight of the aerial vehicle.

        Returns:
            int: The maximum delivery weight.
        """
