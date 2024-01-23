# Write a programe to count total number of odd and even numbers in the given list 

odd_numbers = []
even_numbers = []
numbers=[10,23,20,32]


for value in numbers:
    numbers = int(input("Enter a number: "))

    if numbers % 2 == 0:
        even_numbers.append(numbers)
    else:
        odd_numbers.append(numbers)

print("List of even numbers:", even_numbers)
print("List of odd numbers:", odd_numbers)
