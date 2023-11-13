"""
Assignment 7: Filter List
Submitted by Ricky Espinoza
Submitted:  November 12, 2023

Assignment 7: This assignment introduces two methods (in detail)
              print_filter() - prints a list of sensors that are active and inactive
              change_filter() - allows a user to activate a sensor or deactivate it
              The change_filter() is initiated through the menu prompt #3 choice.
              The change_filter() method will print the filter list showing active or
              inactive states, and it will allow the user to turn a sensor on or off.

Assignment 6: Bubble sort a sensor list but using recursion. Use a test case
              as provided (similar to assignment 5, but with reference to the
              sensor list information from assignment 4).

Assignment 5: A separate recursion assignment (as another project; see assignment 5)

Assignment 4: Apply the use of container objects (lists, tuples, sets, and dictionaries)
              to create and populate some container objects. A container object is needed
              to store information about the sensors that are included in the STEM Center
              dataset. Sensors are thermometers which are placed in various rooms in the
              building and outside the building. Two different container objects will be
              used to store data and a third container object to keep track of which
              sensors.

Assignment 3: Add a menu that provides an interface where a user will use
              to interact with the program. This new code will employ loops
              and conditionals. This is building on the previous assignment
              but will use a new main() to test the menu.

Assignment 2: Add code to prompt the user for a temperature in Celsius
              and then converts that temperature to a specified different temperature
              unit.

Assignment 1: Implement the print_header() that prints the opening
              lines for the STEM Center Project
"""


def print_header_menu():
    """Prints menu for user to see options."""
    """Prints a header."""

    print("\nSTEM Center Temperature Project\nby Ricky Espinoza")
    print("\nMain Menu\n"
          "---------\n"
          "1 - Process a new data file\n"
          "2 - Choose units\n"
          "3 - Edit room filter\n"
          "4 - Show summary statistics\n"
          "5 - Show temperature by date and time\n"
          "6 - Show histogram of temperatures\n"
          "7 - Quit\n")


def user_choice():
    """Checks users input to see if option is a valid one. If not user is prompted again to enter valid option"""

    while True:
        print_header_menu()
        try:
            user_choice = int(input("What is your choice? "))
        except ValueError:
            print("*** Please enter a number only ***")
            continue
        if user_choice == 1:
            new_file(None)
        elif user_choice == 2:
            choose_units()
        elif user_choice == 3:
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
            change_filter(sensors, sensor_list, filter_list)

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


def print_filter(sensor_list, filter_list):
    print("\n")
    sensor_list = recursive_sort(sensor_list)
    for sensor in sensor_list:
        room_number, room_description, sensor_num = sensor
        status = "[ACTIVE]"
        filter_menu = f"{room_number}: {room_description} {status}"
        if sensor_num not in filter_list:
            print(filter_menu[:-8])
        else:
            print(filter_menu)


def change_filter(sensors, sensor_list, filter_list):
    while True:
        print_filter(sensor_list, filter_list)
        try:
            filter_selection = input(
                "\nType the room number to toggle (e.g. 4201) or x to end: ")
        except ValueError:
            print("Invalid Room Number")
            continue
        if filter_selection.lower() == "x":
            break
        else:
            try:
                sensor_number = sensors[filter_selection][1]
            except KeyError:
                print("Invalid Room Number")
                continue

            if sensor_number in filter_list:
                filter_list.remove(sensor_number)
            else:
                filter_list.append(sensor_number)


def new_file(dataset):
    """Open a new file"""
    print("New File Function Called")


def choose_units():
    """Choose unit conversion"""
    print("Choose Units Function Called")


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
    if units == 0:
        return celsius_value
    elif units == 1:
        return (celsius_value * (9/5)) + 32
    elif units == 2:
        return celsius_value + 273.15
    print("*** Invalid Input, the conversion type must be 0, 1, or 2: You entered an illegal value")


def recursive_sort(list_to_sort, key=0):
    """   Recursively takes a list of tuples as input and recursively sorts it in ascending order
    based on the values in the sublists at the specified key index. By default, it sorts the
    sublists based on the values at index 0.
    """

    # created a new list with copied elements from original list
    temp_list = list_to_sort.copy()
    switched = False  # set a flag to check if elements in the list have swtiched

    if len(temp_list) <= 1:  # if the list contains one or zero elements just return the list as is
        return temp_list

    for i in range(len(temp_list) - 1):
        if (key == 0 and temp_list[i][key] > temp_list[i + 1][key]) or (key == 1 and temp_list[i][key] > temp_list[i + 1][key]):
            temp_list[i], temp_list[i + 1] = temp_list[i + 1], temp_list[i]
            switched = True  # if "switched becomes True, a swtich has occurred in the list"

    if not switched:  # if 'switched' is still False, that means no switches occurred
        return temp_list

    return recursive_sort(temp_list[:-1], key) + [temp_list[-1]]


def main():
    """Main is the main program that invokes all functions within program."""

    user_choice()


if __name__ == "__main__":
    main()

"""
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

What is your choice? 3


4201: Foundations Lab [ACTIVE]
4204: CS Lab [ACTIVE]
4205: Tiled Room [ACTIVE]
4213: STEM Center [ACTIVE]
4218: Workshop [ACTIVE]
Out: Outside [ACTIVE]

Type the room number to toggle (e.g. 4201) or x to end: 4201


4201: Foundations Lab 
4204: CS Lab [ACTIVE]
4205: Tiled Room [ACTIVE]
4213: STEM Center [ACTIVE]
4218: Workshop [ACTIVE]
Out: Outside [ACTIVE]

Type the room number to toggle (e.g. 4201) or x to end: 4205


4201: Foundations Lab 
4204: CS Lab [ACTIVE]
4205: Tiled Room 
4213: STEM Center [ACTIVE]
4218: Workshop [ACTIVE]
Out: Outside [ACTIVE]

Type the room number to toggle (e.g. 4201) or x to end: Out


4201: Foundations Lab 
4204: CS Lab [ACTIVE]
4205: Tiled Room 
4213: STEM Center [ACTIVE]
4218: Workshop [ACTIVE]
Out: Outside 

Type the room number to toggle (e.g. 4201) or x to end: Out


4201: Foundations Lab 
4204: CS Lab [ACTIVE]
4205: Tiled Room 
4213: STEM Center [ACTIVE]
4218: Workshop [ACTIVE]
Out: Outside [ACTIVE]

Type the room number to toggle (e.g. 4201) or x to end: 4201


4201: Foundations Lab [ACTIVE]
4204: CS Lab [ACTIVE]
4205: Tiled Room 
4213: STEM Center [ACTIVE]
4218: Workshop [ACTIVE]
Out: Outside [ACTIVE]

Type the room number to toggle (e.g. 4201) or x to end: 4000
Invalid Room Number


4201: Foundations Lab [ACTIVE]
4204: CS Lab [ACTIVE]
4205: Tiled Room 
4213: STEM Center [ACTIVE]
4218: Workshop [ACTIVE]
Out: Outside [ACTIVE]

Type the room number to toggle (e.g. 4201) or x to end: x

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
