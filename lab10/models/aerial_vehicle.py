"""
Abstract class
"""
from abc import ABC, abstractmethod


class AerialVehicle(ABC):
    """Abstract base class for aerial vehicles."""

    def __init__(self, task_variations, manufacturer, max_speed, engine_type):
        """Initialize an aerial vehicle object."""
        self.task_variations = task_variations
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

    def func_with_dict(self, data_type):
        """
            Return a dictionary containing attributes of the specified data type.

            Args:
                data_type (type): The data type to filter the attributes by.

            Returns:
                dict: A dictionary containing attribute names and values that match the specified data type.
        """
        return {key: value for key, value in self.__dict__.items() if isinstance(value, data_type)}

    def __iter__(self):
        return iter(self.task_variations)
