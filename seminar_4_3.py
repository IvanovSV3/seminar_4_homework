# Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности.

import random
number = random.randint(20, 90)
print('ЧИСЛО = ',number)
factor = []

def list_produce(number):           # Задает последовательность чисел
    for i in range(number):
            k = random.randint(0, 99)
            factor.insert(i,k)
            # print(factor)
    return factor

number_list = list_produce(number)
print('Исходный массив - ', number_list)
# print("len = ", range(len(number_list)))


# def list_result(number_list):
for i in range(len(number_list)):
    kk = 0
    for j in range(len(number_list)):
        # print('i', i)
        # print("j",j)
        # print("ii", number_list[i])
        # print("jj", number_list[j])        
        if i != j:
            if number_list[i] == number_list[j]:
                kk = kk + 1
                # print('i', i)
                # print("j",j)
                # print('kk', kk)
                number_list[j] = "delit"
                
print('повторяющиеся эллементы обозначены "delit" = \n', number_list )


itog = []

for f in number_list:
    if  f != "delit":
        itog.append(f)


print('список неповторяющихся элементов =', itog )
