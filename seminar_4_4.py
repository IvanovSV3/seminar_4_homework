# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

n = int(input('задайте степень многочлена - '))

import random
number_k = n
number_k = number_k +1
factor = []
factor_ = []
factor_k = []
factor_1 = []

print('Степень многочлена = ',number_k - 1)
def list_produce(number):           # Задает список коэффициентов
    for i in range(number+1):
            k = random.randint(0, 101)
            factor.insert(i,k)
            # print(factor)
    return factor

def list_produce_X(number):           # Задает список X**
    for i in range(number):
            factor_.insert(i, "X**")
    return factor_


def list_produce_s(number):       # Задает список степеней    
    for i in range(0, number):
        factor_k.insert(i,i)
    return factor_k

def list_plus(number):       # Задает список +    
    for i in range(0, number-1):
        factor_1.insert(i,"+")
    return factor_1


# print('список коэффициентов - ', list_produce(number_k))
# print('список             + = ', list_plus(number_k))
# print('список         иксов - ', list_produce_X(number_k))
list_k = list_produce_s(number_k)
list_k.reverse()
# print('список степеней          - ', list_k)
# itog = []
# itog = list_k + list_produce_X(number_k)
# print(itog)
aa = []
bb = []
cc = []
dd = []
aa = list_k
bb = list_produce_X(number_k)
cc = list_produce(number_k)
dd = list_plus(number_k)
# print("aa", aa)
# print("bb", bb)
# before = itog

#+++++++++++++++++++++++++++

# after = []
# for i in range(number_k):
#     after.append(str(cc[i]) + bb[i] + str(aa[i]) + dd[i])
#     # print(after)

#++++++++++++++++++++++++++++++

after = []
for i in range(number_k):
    if i < number_k-1:
        after.append(str(cc[i]) + bb[i] + str(aa[i]) + dd[i])
    else:
        after.append(str(cc[i]) + bb[i] + str(aa[i]) + " = 0")
    # print(after)
    # print(i)




# print("1",after[0])
# print("bb",bb[0])
# print("aa",aa[0])
# # >>> after
# # ['ab', 'bc', 'cd']
print("многочлен записаный в файл: ", after)

# colors = ['red', 'green', 'blue']
data = open('Ivanov_SV.txt', 'w')
data.writelines(after) # разделителей не будет
data.close()

# rr = []
# rr.append(after[number_k - 1] )
# print('rr', rr)
# print(type(rr))
# rr = str(rr)
# print('rr', rr)
# print(type(rr))

# print(rr.find("+"))
