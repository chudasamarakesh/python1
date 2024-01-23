number = [1, 2, 4, 5, 10]
answer = []
flash = 0  

def getadd(num1, num2):
    global flash 
    while flash < len(number):
        temp = 1
        count = 0
        while count < len(number):
            if count != flash:
                temp = temp * number[count]
            count += 1
        answer.append(temp)
        flash += 1

getadd(1, 2)
print(answer) 
