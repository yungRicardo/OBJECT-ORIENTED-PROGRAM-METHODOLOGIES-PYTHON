"""
Assignment 2: Temperature Conversions
Submitted by Ricky Espinoza
Submitted:  September 28, 2023

Assignment 2: Add code to prompt the user for a temperature in Celsius and then converts that temperature to a specified different temperature unit.
"""

def print_header():
    """Prints a header."""
    print("STEM Center Temperature Project\nby Ricky Espinoza\n")

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

def main():
    """Main is the main program that invokes the print_header function and convert_units function."""
    print_header()
    celsius_value = float(input("Please enter a temperature in degrees Celsius: "))
    units = int(input("Please enter the desired conversion (0 for no conversion, 1 to convert to Fahrenheit, 2 to Kelvin): "))
    convert_units(celsius_value, units)


if __name__ == "__main__":
    main()

r"""
"/Users/rickyespinoza/Desktop/CS 3A Fall 2023/venv/bin/python" /Users/rickyespinoza/Desktop/CS 3A Fall 2023/Assignment_2.py 
STEM Center Temperature Project
by Ricky Espinoza

Please enter a temperature in degrees Celsius: 45
Please enter the desired conversion (0 for no conversion, 1 to convert to Fahrenheit, 2 to Kelvin): 0
That's 45 degrees Celsius

Please enter a temperature in degrees Celsius: 45
Please enter the desired conversion (0 for no conversion, 1 to convert to Fahrenheit, 2 to Kelvin): 1
That's 113.00 degrees Fahrenheit

Please enter a temperature in degrees Celsius: 45
Please enter the desired conversion (0 for no conversion, 1 to convert to Fahrenheit, 2 to Kelvin): 2
That's 318.15 degrees Kelvin

Please enter a temperature in degrees Celsius: 45
Please enter the desired conversion (0 for no conversion, 1 to convert to Fahrenheit, 2 to Kelvin): 3
*** Invalid Input, the conversion type must be 0, 1, or 2: You entered an illegal value
"""



