import random
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
students.sort()
classes = ['Математика', 'Русский язык', 'Информатика']
students_marks = {}
for student in students:
    students_marks[student] = {}
    for class_ in classes:
        marks = [random.randint(1,5) for i in range(3)]
        students_marks[student][class_] = marks
for student in students:
    print(f'''{student}
    {students_marks[student]}''')
print('''Список команд:
        1. Добавить оценку ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Удалить оценку ученика по предмету
        5. Редактировать оценки ученика по предмету
        6. Вывести оценки ученика по всем предметам
        7. Вывести средний балл по каждому предмету для ученика
        8. Проверить допуск ученика к экзамену 
        9. Выход из программы''')
while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        mark = int(input('Введите оценку: '))
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        for student in students:
            print(student)
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        for student in students:
            print(student)
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 4:
        print('4. Удалить оценку ученика по предмету ')
        student = input("Введите имя ученика: ")
        class_ = input("Введите предмет: ")
        mark = int(input("Введите оценку, которую хотите удалить: "))
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            if mark in students_marks[student][class_]:
                students_marks[student][class_].remove(mark)
                print(f'Оценка {mark} ученика {student} по предмету {class_} удалена.')
            else:
                print(f'Оценка {mark} не найдена у ученика {student} по предмету {class_}.')
        else:
            print(f'Ученик "{student}" или предмет "{class_}" не найдены.')
    elif command == 5:
        print('5. Редактировать оценки ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        old_mark = int(input('Введите оценку которую нужно изменить: '))
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            if old_mark in students_marks[student][class_]:
                index = students_marks[student][class_].index(old_mark)
                new_mark = int(input("Введите новую оценку: " ))
                students_marks[student][class_][index] = new_mark
                print(f'Оценка {old_mark} у ученика {student} по предмету {class_} изменена на {new_mark}.')
            else:
                print(f'Оценка {old_mark} не найдена у ученика {student} по предмету {class_}.')
        else:
            print(f'Ученик "{student}" или предмет "{class_}" не найдены')
    elif command == 6:
        print('6. Вывести оценки ученика по всем предметам')
        student = input('Введите имя ученика: ')
        if student in students_marks.keys():
            print(f'Оценки ученика {student} по всем предметам:')
            print(student)
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
                print()
        else:
            print(f'Ученик {student} не найден.')
    elif command == 7:
        print('7. Вывести средний балл для ученика по всем предметам')
        student = input('Введите имя ученика: ')
        if student in students_marks.keys():
            print(f'Средняя оценка ученика {student} по всем предметам:')
            print(student)
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{class_} - {marks_sum // marks_count}')
        else:
            print(f'Ученик {student} не найден.')
    elif command == 8:
        print('8. Проверить допуск ученика к экзамену')
        student = input('Введите имя ученика: ')
        if student in students_marks.keys():
            print(f'Проверка допуска ученика {student} к сдаче экзамена по предметам:')
            print(student)
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                admitt = marks_sum // marks_count
                if admitt >= 3:
                    print(f'{class_} - Допущен')
                else:
                    print(f'{class_} - Не допущен')
        else:
            print(f'Ученик {student} не найден.')
    elif command == 9:
        print('9. Выход из программы')
        break