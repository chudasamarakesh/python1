number = 2
answer = 1

print(number)
print(answer)

while number <= 3000:
   next_number = number + answer
   print(next_number)

   number = answer
   answer = next_number
