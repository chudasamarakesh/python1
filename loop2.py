# Initialize the first two numbers in the sequence
number1 = 0
number2 = 1

# Print the first two numbers
print(number1)
print(number2)

# Generate the sequence up to 10000
while number2 <= 10000:
    # Calculate the next number in the sequence
    next_number = number1 + number2

    # Print the next number
    print(next_number)

    # Update the values for the next iteration
    number1 = number2
    number2 = next_number
