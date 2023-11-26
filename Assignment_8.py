"""
Assignment 8: Dataset Class
Submitted by Ricky Espinoza
Submitted:  November 19, 2023

Assignment 8: Added Class to manage the temperature data. Create a class variable to 
              hold number of TempDataset objects. Implement a getter and setter properties
              for the varibale that holds the name of the dataset. Instantiate instance
              variables to hold data aswell  as adding other instance methods and class methods

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


class TempDataset:

    # class variable to represent number of object created
    temp_obj_created = 0

    def __init__(self):
        self._data_set = None
        self._name = "Unnamed"
        # increment the class variable holding the total number of objects
        TempDataset.temp_obj_created += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if 3 <= len(new_name) <= 20:
            self._name = new_name
        else:
            raise ValueError(
                "Name is too short must bewteen 3 and 20 characters")

    def process_file(self, filename):
        return False

    def get_summary_statistics(self, filter_list):
        if self._data_set == None:
            return None
        else:
            return (0, 0, 0)

    def get_avg_temperature_day_time(self, filter_list, day, time):
        if self._data_set == None:
            return None
        else:
            return 0

    def get_num_temps(self, filter_list, lower_bound, upper_bound):
        if self._data_set == None:
            return None
        else:
            return 0

    def get_loaded_temps(self):
        if self._data_set == None:
            return None
        else:
            return 0

    @classmethod
    def get_num_objects(cls):
        return cls.temp_obj_created


current_set = TempDataset()

print("First test of get_num_objects: ", end='')

if TempDataset.get_num_objects() == 1:
    print("Success")
else:
    print("Fail")

second_set = TempDataset()

print("Second test of get_num_objects: ", end='')

if TempDataset.get_num_objects() == 2:
    print("Success")
else:
    print("Fail")

print("Testing get_name and set_name: ")

print("- Default Name:", end='')

if current_set.name == "Unnamed":
    print("Success")
else:
    print("Fail")

print("- Try setting a name too short: ", end='')

try:
    current_set.name = "to"
    print("Fail")
except ValueError:
    print("Success")

print("- Try setting a name too long: ", end='')

try:
    current_set.name = "supercalifragilisticexpialidocious"
    print("Fail")
except ValueError:
    print("Success")

print("- Try setting a name just right (Goldilocks): ", end='')

try:
    current_set.name = "New Name"
    if current_set.name == "New Name":
        print("Success")
    else:
        print("Fail")
except ValueError:
    print("Fail")

print("- Make sure we didn't touch the other object: ", end='')
if second_set.name == "Unnamed":
    print("Success")
else:
    print("Fail")

print("Testing get_avg_temperature_day_time: ", end='')
if current_set.get_avg_temperature_day_time(None, 0, 0) is None:
    print("Success")
else:
    print("Fail")

print("Testing get_num_temps: ", end='')
if current_set.get_num_temps(None, 0, 0) is None:
    print("Success")
else:
    print("Fail")

print("Testing get_loaded_temps: ", end='')
if current_set.get_loaded_temps() is None:
    print("Success")
else:
    print("Fail")

print("Testing get_summary_statistics: ", end='')
if current_set.get_summary_statistics(None) is None:
    print("Success")
else:
    print("Fail")

print("Testing process_file: ", end='')
if current_set.process_file(None) is False:
    print("Success")
else:
    print("Fail")


"""
SAMPLE RUN

First test of get_num_objects: Success
Second test of get_num_objects: Success
Testing get_name and set_name:
- Default Name:Success
- Try setting a name too short: Success
- Try setting a name too long: Success
- Try setting a name just right (Goldilocks): Success
- Make sure we didn't touch the other object: Success
Testing get_avg_temperature_day_time: Success
Testing get_num_temps: Success
Testing get_loaded_temps: Success
Testing get_summary_statistics: Success
Testing process_file: Success
"""
