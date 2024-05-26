from enum import Enum
import json
import os
from icecream import ic

garage = []

class Actions(Enum):
    ADD = 1
    DELETE = 2
    PRINT = 3
    UPDATE = 4
    EXIT = 5 
    COUNT_CARS = 6
    NULIFY_CARS_ARRAY = 7

def menu():
    ic("Displaying menu options:")  # Corrected print statement
    # Display all available actions
    for action in Actions:
        ic(f'{action.value} - {action.name}')
    # Return the selected action as an enum member
    return Actions(int(input("Please select an action: ")))

def add_car():
    garage.append({'brand': input("What brand? "), 'model': int(input("What model? ")), 'color': input("What color? ")})

def print_cars():
    if not garage:
        ic("The garage is empty.")
    for index, car in enumerate(garage):
        ic(f"({index}) brand: {car['brand']}, model: {car['model']}, color: {car['color']}")

def upd_car():
    car_number = find_car()
    garage[car_number] = {'brand': input("What brand? "), 'model': int(input("What model? ")), 'color': input("What color? ")}

def del_car():
    car_number = find_car()
    ic(f'{garage[car_number]} was deleted')
    garage.pop(car_number)

def find_car():
    print_cars()
    car_number = int(input("Please select a car number: "))
    return car_number

def save_garage_to_json(garage, filename):
    with open(filename, 'w') as f:
        ic(garage)
        json.dump(garage, f)

def load_garage_from_json(filename):
    if not os.path.exists(filename):
        return []  # Return an empty list if the file does not exist
    try:
        with open(filename, 'r') as f:
            return ic(json.load(f))
    except json.JSONDecodeError:
        return []  # Return an empty list if the file is empty or contains invalid JSON

def count_cars():
    ic(f"There are {len(garage)} cars in the garage.")

def nulify_cars_array():
    confirmation = input("Are you sure you want to delete all the cars from the garage? (yes/no): ").strip().lower()
    if confirmation == 'yes':
        garage.clear()
        ic("All cars have been deleted from the garage.")
    else:
        ic("Operation cancelled. No cars were deleted.")

if __name__ == "__main__":
    ic("Loading garage data...")  # Ensure this line is executed
    garage = load_garage_from_json('garage.json')
    while True:
        user_selection = menu()
        ic(f"User selected action: {user_selection}")
        if user_selection == Actions.EXIT:
            save_garage_to_json(garage, 'garage.json')
            exit()
        elif user_selection == Actions.ADD:
            add_car()
        elif user_selection == Actions.PRINT:
            print_cars()
        elif user_selection == Actions.DELETE:
            del_car()
        elif user_selection == Actions.UPDATE:
            upd_car()
        elif user_selection == Actions.COUNT_CARS:
            count_cars()
        elif user_selection == Actions.NULIFY_CARS_ARRAY:
            nulify_cars_array()
