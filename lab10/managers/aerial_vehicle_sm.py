"""
Class AerialVehicleManagerSM

A class for managing aerial vehicles with a specific structure.

Attributes:
    regular_manager (AerialVehicleManager): The regular AerialVehicleManager object.
    index (int): The index used for iteration.

Methods:
    __init__(self, regular_manager): Initializes the AerialVehicleManagerSM class.
    __iter__(self): Returns an iterator for the task variations of the aerial vehicles.
    __len__(self): Returns the total length of the task variations.
    __getitem__(self, index): Returns the task variations at the specified index.
    __next__(self): Returns the next aerial vehicle in the iteration.

"""


class AerialVehicleManagerSM:
    """A class for managing aerial vehicles with a specific structure."""
    def __init__(self, regular_manager):
        """Initialize the AerialVehicleManagerIterator class."""
        self.regular_manager = regular_manager
        self.index = 0

    def __iter__(self):
        return self

    def __len__(self):
        length = 0
        for element in self.regular_manager.aerial_vehicles:
            length += len(getattr(element, "task_variation", ""))
        return length

    def __getitem__(self, index):
        return getattr(self.regular_manager.aerial_vehicles[index], "task_variations")

    def __next__(self):
        if self.index >= len(self.regular_manager.aerial_vehicles):
            self.index = 0
            raise StopIteration
        value = self.regular_manager.aerial_vehicles[self.index]
        self.index += 1
        return value
