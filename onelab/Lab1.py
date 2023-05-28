#Лабораторная работа №1

import random as r


def algoritm1(nums_al):
    cnt = 0
    j = 0
    i = 0
    while i < len(nums_al):
        if i >= len(nums_al): return nums_al
        cnt = 0
        if nums_al[i]%2 == 0:
            cnt = 0
            i += 1
            continue
        elif nums_al[i]%2 != 0:
            j = i
            while j < len(nums_al):
                if nums_al[j] % 2 != 0:
                    cnt += 1
                else:
                    break
                j += 1
            if cnt == 1:
                del nums_al[i]
            elif cnt == 2:
                del nums_al[i]
                del nums_al[i]
            elif cnt > 2:
                i += cnt
    return nums_al


def algoritm2(nums_al):
    cnt = 0
    j = 0
    i = 0
    list2 = []
    while i <= len(nums_al):
        cnt = 0
        if i >= len(nums_al): return list2
        if nums_al[i]%2 == 0:
            list2.append(nums_al[i])
            i += 1
            continue
        if nums_al[i]%2 != 0:
            j = i
            while j < len(nums_al):
               if nums_al[j]%2 != 0:
                   cnt += 1
               else: break
               j += 1
            if cnt <= 2:
                i += cnt
                cnt = 0
            else:
                j = i
                k = cnt
                while j < len(nums_al):
                    k -= 1
                    list2.append(nums_al[j])
                    if k == 0: break
                    j += 1
        i += cnt
    return list2


def prov_bool():
    return True if bool_1 else False


def prov_list(lst):
    for i in lst:
        if not i.isnumeric():
            print("В списке могут быть только числа")
            return False
        else:
            return True


n = int(input('Введите количество элементов списка:'))
list1 = []
bool_1 = True
k = int(input('Для ввода чисел с клавиатуры введите 1, для заполнения списка случайными числами введите 2:'))

if k == 1:
    for i in range(n):
        string = "Введите " + str(i+1)+" элемент списка: "
        list1.append(input(string))
    bool_1 = prov_list(list1)
elif k == 2:
        diap1 = int(input('Введите начало диапазона случайных чисел: '))
        diap2 = int(input('Введите конец диапазона случайных чисел: '))
        list1 = [r.randint(diap1, diap2) for x in range(n)]

if prov_bool():
    nums = [int(x) for x in list1]
    nums2 = [int(x) for x in list1]

    print('До: ', nums)
    print('После (алгоритм первый):  ', algoritm1(nums2))
    print('После (алгоритм второй):  ', algoritm2(nums))