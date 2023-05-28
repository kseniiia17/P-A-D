# лабораторная работа №2
import numpy as np

# поиск минимального числа в столбце
def find_min(n1, m1, k1, matrix):
    mini = matrix[0][k1]
    for i in range(n1):
        for j in range(m1):
            if j != k1:
                continue
            else:
                if matrix[i][j] < mini:
                    mini = matrix[i][j]
    return mini

# запись данных из файла
def write(array, f1):
    for i in array:
        print(" ".join(map(str, i)), file=f1)


n, m = map(int, input('Введите количество строк и столбцов: ').split())
start, end = map(int, input('Введите начальное и конечное значения диапазона: ').split())
k = int(input('Введите номер столбца для нахождения в нем минимального элемента: ')) - 1
matrix1 = np.random.randint(start, end, (n, m))

f = open('main.txt', 'w')

f.write("Line = "+str(n)+"\n")
f.write("Column = "+str(m)+"\n")
rez = find_min(n, m, k, matrix1)
write(matrix1, f)
f.write("Min element "+str(k+1)+" column: "+str(rez))

f.close()




