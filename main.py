import random
    # 1
# 2
def summch(list1):
    sum = 0
    for i in list1:
        if i % 2 == 0:
            sum += i
    print("Сумма чисел равна: ", sum)
# 1
def summotr(list1):
    sum = 0
    for i in list1:
        if i<0:
            sum += i
    print("Сумма отрицательных чисел равна: ", sum)
# 3
def summnech(list1):
    sum = 0
    for i in list1:
        if i % 2 != 0:
            sum += i
    print("Сумма нечетных чисел равна: ", sum)
    return sum
# 4
def pr3(list1):
    pr = 1
    for i in range(len(list1)):
        if i % 3 == 0:
            pr *= list1[i]
    print("Произведение элементов с индексами кратными 3 равен: ", pr)
    return pr
# 5
def prminmax(list1):
    max1 = max(list1)
    min1 = min(list1)
    maxindex = list1.index(max1, 0, len(list1))
    minindex = list1.index(min1, 0, len(list1))
    pr = 1
    if maxindex < minindex:
        for i in range(maxindex, minindex):
            pr *= list1[i]
    else:
        for i in range(minindex, maxindex):
            pr *= list1[i]
    print("Произведение элементов между минимальным и максимальным элементом: ", pr)
# 6
def summinmax(list1):
    i = len(list1) - 1
    b = 0
    sum = 0
    while(i!=0):
        if list1[i] > 0:
            b = i
            break
        i -= 1
    j = 0
    a = 0
    while (j!=len(list1)-1):
        if list1[j] > 0:
            a = j
            break
        j += 1
    for i in range(a+1, b):
        sum += list1[i]
    print(a, b)
    print("Сумму элементов, находящихся между первым и последним положительными элементами: ", sum)
list1 = [random.randint(-10,10) for i in range(10)]
print(list1)
summch(list1)
summotr(list1)
summnech(list1)
pr3(list1)
prminmax(list1)
summinmax(list1)

    # 2
# 1
def spisok1(list2):
    value = []
    for i in list2:
        if i % 2 == 0:
            value.append(i)
    print("Четные числа  ", value)
# 2
def spisok2(list2):
    value = []
    for i in list2:
        if i % 2 != 0:
            value.append(i)
    print("Нечетные числа: ", value)
# 3
def spisok3(list2):
    value = []
    for i in list2:
        if i < 0:
            value.append(i)
    print("Отрицательные числа: ", value)
# 4
def spisok4(list2):
    value = []
    for i in list2:
        if i >= 0:
            value.append(i)
    print("Положительные числа: ", value)
list2 = [random.randint(-10,10) for i in range(10)]
print(list2)
spisok1(list2)
spisok2(list2)
spisok3(list2)
spisok4(list2)