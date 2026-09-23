# Ask the user to enter temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit = (celsius * 9 / 5) + 32

# Display Fahrenheit rounded to 2 decimal places
print("Temperature in Fahrenheit:", round(fahrenheit, 2))

# Classify the temperature
if celsius < 15:
    print("Temperature Level: Cold")
elif celsius <= 30:
    print("Temperature Level: Normal")
else:
    print("Temperature Level: Hot")