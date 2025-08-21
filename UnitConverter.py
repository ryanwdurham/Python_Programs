def miles_to_km(miles):
    return miles * 1.60934

def km_to_miles(km):
    return km / 1.60934

def lbs_to_kg(lbs):
    return lbs * 0.453592

def kg_to_lbs(kg):
    return kg / 0.453592

def c_to_f(celsius):
    return (celsius * 9/5) + 32

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9


print("Welcome to my simple Unit Converter!")
print("Choose a conversion:")
print("1. Miles to Kilometers")
print("2. Kilometers to Miles")
print("3. Pounds to Kilograms")
print("4. Kilograms to Pounds")
print("5. Celsius to Fahrenheit")
print("6. Fahrenheit to Celsius")

while True:
    choice = input("Enter choice (1-6) or 'q' to quit: ")

    if choice.lower() == "q":
        print("Goodbye!")
        break

    if choice not in ("1", "2", "3", "4", "5", "6"):
        print("Invalid choice, try again.")
        continue

    try:
        value = float(input("Enter value to convert: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == "1":
        print(f"{value} miles = {miles_to_km(value):.2f} km")
    elif choice == "2":
        print(f"{value} km = {km_to_miles(value):.2f} miles")
    elif choice == "3":
        print(f"{value} lbs = {lbs_to_kg(value):.2f} kg")
    elif choice == "4":
        print(f"{value} kg = {kg_to_lbs(value):.2f} lbs")
    elif choice == "5":
        print(f"{value}°C = {c_to_f(value):.2f}°F")
    elif choice == "6":
        print(f"{value}°F = {f_to_c(value):.2f}°C")

    print("-----------------------------")