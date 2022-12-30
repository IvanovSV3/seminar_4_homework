# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

fail_1 = []
fail_2 = []

data = open('Ivanov_SV.txt', 'r')
fail_1 = data.read()
data.close()
print(fail_1)

data = open('Ivanov_SV_1.txt', 'r')
fail_2 = data.read()
data.close()
print(fail_2)
#================================================= 

print(fail_2.split("+"))
temp_1 = []
temp_2 = []
temp_1 = fail_2.split("+")
print('temp_1 = ', temp_1)
print(temp_1[0])
temp_2 = temp_1[0]
# print("temp_2 = ", temp_2.split("X**"))
temp_3 = temp_2.split("X**")
print('temp_3 =', temp_3)
kk = int(temp_3[0])
print(kk)
kk_number = int(temp_3[1])
print('степень многочлена kk_num = ', kk_number)
# for i in fail_2:
#     # print(i)

for i in range(kk_number):
    temp_3.append(temp_1[i].split("X**"))
    print('44',temp_3[i])
print(temp_3)
print("ДАЛЬШЕ НЕ СМОГ!")