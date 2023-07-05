def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

print("Temperature Converter")
print("---------------------")

while True:
    print("\n1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print("3. Quit")

    choice = input("\nEnter your choice (1-3): ")

    if choice == "1":
        f = float(input("Enter temperature in Fahrenheit: "))
        c = fahrenheit_to_celsius(f)
        print(f"{f}°F is equal to {c}°C")
    elif choice == "2":
        c = float(input("Enter temperature in Celsius: "))
        f = celsius_to_fahrenheit(c)
        print(f"{c}°C is equal to {f}°F")
    elif choice == "3":
        print("Enjoy the Weather")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 3.")
