# Лабораторная работа №4

import os
from pathlib import Path
import csv


class Human(object):
    "Базовый класс для определения человека"

    # инициализация свойств - конструктор
    def __init__(self, name, age, gender):
        self.name = name
        self.__age = age
        self.gender = gender

    # замена имени
    def set_name(self, name):
        if name.istitle() == 'True':
            self.name = name

    # получение имени
    def get_name(self):
        return self.name

    def set_age(self, age):
        if 0 <= age <= 65:
            self.__age = age

    def get_age(self):
        return self.__age

    @staticmethod
    def is_adult(age):
        if age >= 18:
            return age

    def set_gender(self, gender):
        if gender == "male":
            self.gender = gender
        elif gender == "female":
            self.gender = gender

    def get_gender(self):
        return self.gender

# наследуется от Human
class OfficeWorker(Human):
    def __init__(self, id, name, age, gender, post, workplace_sign):
        Human.__init__(self, name, age, gender)
        self.id = id
        self.post = post
        self.workplace_sign = workplace_sign
        # передвижение
        self.movements = []

    def set_post(self, post):
        self.post = post

    def get_post(self):
        return self.post

    # дата передвижения
    def movement(self, date):
        self.movements.append(date)

    # метод итератора, который перебирает элементы листа movement
    def __iter__(self):
        return OfficeIterator(self.movements)

    # вывод информации о рабочем
    def __repr__(self):
        return f'Office Worker № {self.id}, {self.name}, {self.post}, {self.workplace_sign}'

    def generator(self, i):
        while i < len(self.movements):
            yield self.movements[i]
            i += 1
        else:
            yield 0

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, item):
        s = "Worker" + item
        return self.__dict__[s]


class OfficeIterator:
    def __init__(self, movements, start=0):
        OfficeWorker.__init__(self, movements)
        self.movements = movements
        self.movements_count = start

    def __next__(self):
        if self.movements_count < len(self.movements):
            date = self.movements[self.movements_count]
            self.movements_count += 1
            return date
        else:
            return 0

    def __iter__(self):
        return self


office_worker1 = OfficeWorker(0, "Pop", "20", "male", "intern", "OK")
print(office_worker1.__repr__())



def get_history_to_dict(move_history):
    print("movement number; date and time; workplace sign; room number")
    with open("movement_history.csv", "r", encoding='utf-8') as f1:
        reader = csv.reader(f1)
        for row in reader:
            print(*row)
            move_history[row[0]] = row[1:]


def get_workers_base(workers_base):
    print("id; name; age; gender; post; workplace_sign")
    with open('Office_workers.csv', 'r', encoding='utf-8') as f2:
        reader = csv.reader(f2)
        for row in reader:
            print(*row)
            workers_base[row[0]] = row[1:]


def sort_id(workers_base):
    print("\nОтсортируем словарь по идентификатору работников: ")
    for elem in sorted(workers_base.items(), key=lambda para: int(para[0][0])):
        print(elem[0], *elem[1])


def sort_movement_number(move_history):
    print("\nОтсортируем словарь по номеру комнаты работников: ")
    # sortMoveHistory = dict(sorted(moveHistory.items(), key=lambda item: item[2]))
    for elem in sorted(move_history.items(), key=lambda para: int(para[1][2])):
        print(elem[0], *elem[1])


def sort_movement_str(move_history):
    print("\nОтсортируем словарь по признаку рабочего стола работников: ")
    # sortMoveHistory = dict(sorted(moveHistory.items(), key=lambda item: item[2]))
    for elem in sorted(move_history.items(), key=lambda para: para[1][1]):
        print(elem[0], *elem[1])
    print("")


def output_by_criterion(move_history):
    criterion = input("Введите признак рабочего стола: \n")
    print(f'\nСтроки, в которых признак рабочего стола "{criterion}": ')
    for elem in move_history:
        if move_history[elem][1] == criterion:
            print(elem, *move_history[elem])


def write_to_history(move_history):
    newKey = input("Введите номер перемещения (ключ): ")
    newDate = input("Введите дату и время через точку с запятой: ")
    newWorkplaceSign = input("Введите признак рабочего стола: ")
    newRoomNumber = input("Введите номер комнаты: ")
    move_history[newKey] = [newDate, newWorkplaceSign, newRoomNumber]
    with open('movement_history.csv', 'w', encoding='utf-8') as f:
        for elem in move_history:
            f.write(elem + ',' + move_history[elem][0] + ',' + move_history[elem][1] + ',' + move_history[elem][2] + '\n')


def write_to_base(workers_base):
    new_id = input("Введите идентификатор работника (id): ")
    new_name = input("Введите имя сотрудника: ")
    new_age = input("Введите возраст сотрудника: ")
    new_gender = input("Введите пол сотрудника: ")
    new_post = input("Введите должность сотрудника: ")
    new_workplace_sign = input("Введите признак рабочего стола: ")
    workers_base[new_id] = [new_name, new_age, new_gender, new_post, new_workplace_sign]
    with open('Office_workers.csv', "w", encoding='utf-8') as f2:
        for elem in workers_base:
            f2.write(elem + ',' + workers_base[elem][0] + ',' + workers_base[elem][1] + ',' + workers_base[elem][2]
                     + ',' + workers_base[elem][3] + ',' + workers_base[elem][4] + '\n')




# main
def main():
    # countFiles()
    version = int(input("1. Работа с историей перемещения;\n2. Работа с базой сотрудников\nВведите нужный вариант: "))
    match version:
        case 1:
            move_history = {}
            get_history_to_dict(move_history)
            sort_movement_number(move_history)
            sort_movement_str(move_history)
            output_by_criterion(move_history)
            write_to_history(move_history)
        case 2:
            workers_base = {}
            get_workers_base(workers_base)
            sort_id(workers_base)
            write_to_base(workers_base)


if __name__ == "__main__":
    main()

