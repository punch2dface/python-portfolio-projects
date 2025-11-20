# Unit Converter
# Convert between different units of measurement
# This supports Celsius to Fahrenheit, Kilometers to Miles, and Kilograms to Pounds.

# Celsius to Fahrenheit Function
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Fahrenheit to Celsius Function
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Kilometers to Miles Function
def kilometers_to_miles(kilometers):
    miles = kilometers * 0.621371
    return miles

# Miles to Kilometers Function
def miles_to_kilometers(miles):
    kilometers = miles / 0.621371
    return kilometers

# Kilograms to Pounds Function
def kilograms_to_pounds(kilograms):
    pounds = kilograms * 2.20462
    return pounds

# Pounds to Kilograms Function
def pounds_to_kilograms(pounds):
    kilograms = pounds / 2.20462
    return kilograms

# main function to demonstrate the conversions
def main():
    print("Unit Converter")
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    print("3. KM → Miles")
    print("4. Miles → KM")
    print("5. KG → Pounds")
    print("6. Pounds → KG")
    
    choice = int(input("Choose an option: "))
    value = float(input("Enter the value: "))
    
    if choice == 1:
        print(celsius_to_fahrenheit(value))
    elif choice == 2:
        print(fahrenheit_to_celsius(value))
    elif choice == 3:
        print(kilometers_to_miles(value))
    elif choice == 4:
        print(miles_to_kilometers(value))
    elif choice == 5:
        print(kilograms_to_pounds(value))
    elif choice == 6:
        print(pounds_to_kilograms(value))
    else:
        print("Invalid Choice")

if __name__ == "__main__":
    main()
    