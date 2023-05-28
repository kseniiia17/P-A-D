# Лабораторная работа №3

import os

# выгрузка данных из файла
def file_open(animals):
    with open("data.csv",'r', encoding="utf-8") as f:
        for line in f:
            (key, name, kind, age) = line.split(",")
            value = {
               'name': name,
               'breed': kind,
               'age': age,
            }
            animals[int(key)] = value
    f.close()
    return animals

# Животные, которым больше 5 лет
def condition(animals):
    with open("data.csv", 'a', encoding='utf-8') as f:
        f.write('\nЖивотные старше пяти лет:\n')
        for k, v in animals.items():
            age_2 = v['age']
            if int(age_2) > 5:
                f.write(f'№{k}: {v}\n')
                #print(f'№{k}: {v}')

# подсчет количества файлов в папке проекта
def file_cnt():
    file_count = sum(len(files) for _, _, files in os.walk(r'C:\Users\kv0lk\PycharmProjects\pythonProject3'))
    print("\nFiles: ", file_count, file=f)


animal = {}
animal = file_open(animal)


# сортировка введенного словаря
with open("data.csv", 'a', encoding='utf-8') as f:
    file_cnt()
    print('Cортировка словаря:', file=f)
    sorted_tuple = sorted(animal.items(), key=lambda x: x[0])
    for k, v in sorted_tuple:
        print(f'№{k}: {v}', file=f)

condition(animal)