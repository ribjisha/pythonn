# Program to validate input and display number in different formats

# Ask user for input
num_str = input("Enter a positive integer with at least 3 digits: ")

# Validate input
if not num_str.isdigit():
    print("Please enter a valid positive number.")
else:
    num = int(num_str)

    if num <= 0:
        print("Please enter a positive number.")
    elif num < 100:
        print("Please enter a number with at least 3 digits.")
    else:
        # Display results
        print("Decimal format:", num)
        print("Binary format:", bin(num))
        print("Octal format:", oct(num))
        print("Hexadecimal format:", hex(num))

        # Last digit
        last_digit = num % 10
        print("Last digit:", last_digit)

        # Even or Odd
        if num % 2 == 0:
            print("The number is Even.")
        else:
            print("The number is Odd.")
