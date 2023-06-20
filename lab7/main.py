"""
Main file to create objects and validate methods
"""
from helicopter import Helicopter


if __name__ == "__main__":
    """
    Creates a list of helicopter objects and prints their details.
    """

    helicopters = [
        Helicopter(),
        Helicopter("MI-24", 0, 800, 200, 50),
        Helicopter.get_instance(),
        Helicopter.get_instance()
    ]

    for helicopter in helicopters:
        """
        Prints the details of each helicopter object.
        
        Parameters:
        - helicopter (Helicopter): The helicopter object to be printed.
        """

        print(helicopter)
