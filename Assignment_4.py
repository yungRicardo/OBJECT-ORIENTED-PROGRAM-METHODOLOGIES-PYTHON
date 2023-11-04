"""
Assignment 4: Creating a Sensor List and Filter List
Submitted by Ricky Espinoza
Submitted:  October 11, 2023
"""

def print_header():
    """Prints a header."""
    print("\nSTEM Center Temperature Project\nby Ricky Espinoza")

def print_menu():
    """Prints menu for user to see options."""
    print("\nMain Menu\n"
          "---------\n"
          "1 - Process a new data file\n"
          "2 - Choose units\n"
          "3 - Edit room filter\n"
          "4 - Show summary statistics\n"
          "5 - Show temperature by date and time\n"
          "6 - Show histogram of temperatures\n"
          "7 - Quit")
def user_choice():
    """Checks users input to see if option is a valid one. If not user is prompted again to enter valid option"""

    while True:
        print_menu()
        try:
            user_choice = int(input("\nWhat is your choice? "))

        except ValueError:
            print("*** Please enter a number only ***")
            continue

        if user_choice == 1:
            new_file(None)
        elif user_choice == 2:
            choose_units()
        elif user_choice == 3:
            change_filter(None, None)
        elif user_choice == 4:
            print_summary_statistics(None, None)
        elif user_choice == 5:
            print_temp_by_day_time(None, None)
        elif user_choice == 6:
            print_histogram(None, None)
        elif user_choice == 7:
            print("Thank you for using the STEM Center Temperature Project\n\n")
            break
        else:
            print("Invalid Choice, please enter an integer between 1 and 7.\n\n")

def new_file(dataset):
    """Open a new file"""
    print("New File Function Called")

def choose_units():
    """Choose unit conversion"""
    print("Choose Units Function Called")

def change_filter(sensor_list, active_sensors):
    """Change filter"""
    print("Change Filter Function Called")

def print_summary_statistics(dataset, active_sensors):
    """Print summary statistics"""
    print("Summary Statistics Function Called")

def print_temp_by_day_time(dataset, active_sensors):
    """Print temp by daytime"""
    print("Print Temp by Day/Time Function Called")

def print_histogram(dataset, active_sensors):
    """Print histogram"""
    print("Print Histogram Function Called")

def convert_units(celsius_value, units):
    """Converts Celsius to Fahrenheit or Kelvin depending on unit selected"""
    fahrenheit_value = ((celsius_value * 9/5) + 32)
    kelvin_value = (celsius_value + 273.15)
    if units == 0:
        print(f"That's {int(celsius_value)} degrees Celsius")
    elif units == 1:
        print(f"That's {fahrenheit_value:.2f} degrees Fahrenheit")
    elif units == 2:
        print(f"That's {kelvin_value:.2f} degrees Kelvin")
    else:
        print("*** Invalid Input, the conversion type must be 0, 1, or 2: You entered an illegal value")

def testing_sensors(sensors, sensor_list, filter_list):
    """
    Conducts a series of tests to ensure that the provided `sensors`, `sensor_list`, and `filter_list` are
    correctly set up and consistent with each other.
    """
    print("\n\nTesting sensors:")
    if sensors["4213"][0] == "STEM Center" and sensors["Out"][1] == 5:
        print("Pass")
    else:
        print("Fail")

    print("Testing sensor_list length:")
    if len(sensor_list) == 6:
        print("Pass")
        print("Testing sensor_list content:")
        for item in sensor_list:
            if item[1] != sensors[item[0]][0]:
                print("Fail")
                break
        else:
            print("Pass")

    print("Testing filter_list length:")
    if len(filter_list) == 6:
        print("Pass")
    else:
        print("Fail")

    print("Testing filter_list content:")
    if sum(filter_list) == 15:
        print("Pass")
    else:
        print("Fail")

def main():
    """Main is the main program that invokes all functions within program."""

    sensors = {
        "4213": ("STEM Center", 0),
        "4201": ("Foundations Lab", 1),
        "4204": ("CS Lab", 2),
        "4218": ("Workshop", 3),
        "4205": ("Tiled Room", 4),
        "Out": ("Outside", 5)
    }
    sensor_list = [(key,) + value for key, value in sensors.items()]
    filter_list = [value[1] for value in sensors.values()]
    testing_sensors(sensors, sensor_list, filter_list)
    print_header()
    user_choice()

if __name__ == "__main__":
    main()

"""
SAMPLE RUN

Testing sensors:
Pass
Testing sensor_list length:
Pass
Testing sensor_list content:
Pass
Testing filter_list length:
Pass
Testing filter_list content:
Pass

STEM Center Temperature Project
by Ricky Espinoza

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

What is your choice? 7
Thank you for using the STEM Center Temperature Project
"""

