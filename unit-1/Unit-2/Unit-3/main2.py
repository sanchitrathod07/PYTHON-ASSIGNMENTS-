import celsius_to_fahrenheit
import fahrenheit_to_celsius
import celsius_to_kelvin
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
choice = int(input("Enter choice: "))
if choice == 1:
    c = float(input("Enter Celsius: "))
    print("Fahrenheit:", celsius_to_fahrenheit.convert(c))

elif choice == 2:
    f = float(input("Enter Fahrenheit: "))
    print("Celsius:", fahrenheit_to_celsius.convert(f))

elif choice == 3:
    c = float(input("Enter Celsius: "))
    print("Kelvin:", celsius_to_kelvin.convert(c))
else:
    print("Invalid choice")
