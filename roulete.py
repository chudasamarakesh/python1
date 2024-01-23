import random

number=int(input("enter the number:"))
print("user output",number)

answer=random.randint(1,10)
print("server output",answer)

if number==answer:
    print("Congratulations! You win!")
else:
    print("Bad luck, next time")