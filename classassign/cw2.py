# Ask the user to enter a string
text = input("Enter a string: ")

# Encrypt the string
encrypted = ""

for i in range(len(text)):
    # Convert character to ASCII value
    ascii_value = ord(text[i])

    # Modify ASCII value according to position
    if i % 2 == 0:
        ascii_value += 2
    else:
        ascii_value -= 2

    # Convert modified ASCII value back to character
    encrypted += chr(ascii_value)

    # Print the modified ASCII value
    print("Modified ASCII value:", ascii_value)

# Display the encrypted string
print("Encrypted string:", encrypted)