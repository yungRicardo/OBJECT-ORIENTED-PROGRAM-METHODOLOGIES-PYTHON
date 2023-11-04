

def print_header():
    """Prints a header."""
    print("\n\nSTEM Center Temperature Project\nby Ricky Espinoza\n")


def print_menu():
    """Prints a menu"""
    print("\nMain Menu"
          "\n---------"
          "\n1 - Process a new data file"
          "\n2 - Choose units"
          "\n3 - Edit room filter"
          "\n4 - Show summary statistics"
          "\n5 - Show temperature by date and time"
          "\n6 - Show histogram of temperatures"
          "\n7 - Quit")


def user_selection():
    while True:
        print_menu()
        try:
            user_option = int(input("\nWhat is your choice? "))
        except ValueError:
            print("*** Please enter a number only ***")
            continue
        if user_option == 1:
            new_file(None)
        elif user_option == 2:
            choose_units()
        elif user_option == 3:
            change_filter(None, None)
        elif user_option == 4:
            print_summary(None, None)
        elif user_option == 5:
            print_temp_by_day_time(None, None)
        elif user_option == 6:
            print_histogram(None, None)
        elif user_option == 7:
            print("Thank you for using the STEM Center Temperature Project")
            break
        else:
            print("Invalid Choice, please enter an integer between 1 and 7")


def new_file(dataset):
    """Open a new file."""
    print("New file function called")


def choose_units():
    """Choose unit of conversion."""
    print("Choose Units function called")


def change_filter(senosr_list, active_sensors):
    """Change filter"""
    print("Change Filter function called")


def print_summary(dataset, active_sensors):
    """print summary"""
    print("Summary Statistics function called")


def print_temp_by_day_time(dataset, active_sensors):
    """print temperature by daytime"""
    print("Print Temp by Day/Time function called")


def print_histogram(dataset, activee_sensors):
    """print histogram data"""
    print("Print Histogram function called")


def convert_units(celsius_value, units):
    """Converts Celsius to Fahrenheit or Kelvin depending on unit selected"""
    fahrenheit_value = ((celsius_value * 9/5) + 32)
    kelvin_value = (celsius_value + 273.15)
    if units == 0:
        print(f"That's {int(celsius_value)} degrees Celsius")
    elif units == 1:
        print(f"That's {fahrenheit_value: .2f} degrees Fahrenheit")
    elif units == 2:
        print(f"That's {kelvin_value: .2f} degrees Kelvin")
    else:
        print("*** Invalid Input, the conversion type must be 0, 1, or 2: You entered an illegal value")


def main():
    print_header()
    user_selection()


if __name__ == "__main__":
    main()
