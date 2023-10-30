print("Enter '1' to convert from Celsius to Fahrenheit")
print("Enter '2' to convert from Fahrenheit to Celsius")

choice = input("Enter your choice (1/2): ")

if choice == '1':
    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = (celsius * 1.8) + 32
    print(f"{celsius}°C is equal to {fahrenheit}°F")
elif choice == '2':
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) / 1.8
    print(f"{fahrenheit}°F is equal to {celsius}°C")
else:
    print("Invalid option entered.")
