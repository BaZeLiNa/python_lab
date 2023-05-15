from helicopter import Helicopter

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
if __name__ == "__main__":
    helicopters = [
        Helicopter(),
        Helicopter("MI-24", 0, 800, 200, 50),
        Helicopter.get_instance(),
        Helicopter.get_instance()
    ]

    for helicopter in helicopters:
        print(helicopter)
