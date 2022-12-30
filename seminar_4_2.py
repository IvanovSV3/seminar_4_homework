# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.
import random
number = random.randint(2, 20)
print('ЧИСЛО = ',number)
factor = []

def multi(number):
    for i in range(2, number +1 ):
        # print(i)
        if number % i == 0:
            factor.insert(i,i)
            # print(factor)
    return factor

print('Множители чесла - ', multi(number))