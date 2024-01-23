
#otp generator

from random import choice
import random


def generateotp():
    
    answer=str(random.randint(10,99))+str(random.randint(10,99))+str(random.randint(10,99))
    print(answer)
    

def generatealph():
    
    alphabet=['a','v','s','f','g','j','r','w','k']
    answer=choice(alphabet)+choice(alphabet)+choice(alphabet)
    print(answer)
    

generatealph()