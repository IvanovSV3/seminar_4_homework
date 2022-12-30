# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

d = 0.0000001
number = 9/7
print("Исходное число = ",number)
print('точность = ', d)

number_temp = number + d
number_str = str(number)
number_temp = str(number_temp) # число измененное на погрешность

def number_new(number_str, number_temp): # перебераем исходное число до первого измененного элемента
    i = 0
    numbet_itog = []
    for k in number_str:    
        if number_str[i] == number_temp[i]:
            numbet_itog.insert(i, number_str[i])
            i = i + 1
        else:
            numbet_itog.insert(i, number_str[i])
            break
    return numbet_itog

print("itog = ", number_new(number_str, number_temp))
numder_ = number_new(number_str, number_temp)
numder_ = ''.join(numder_)                             # склеиваем стоку в число
print("число с заданной точностью = ",numder_)