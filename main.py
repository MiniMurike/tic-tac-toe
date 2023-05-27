def print_table():
    """Печать игровой сетки"""
    for i in range(4):
        for j in range(4):
            if not (i or j):    print(' ', end=' ')                     # Если угловая позиция, то печать "ничего"
            elif not i:         print(j - 1, end=' ')                   # Если это первая строка, то печатаем шапку
            elif not j:         print(i - 1, end=' ')                   # Если это первый элемент в строке, то печатаем шапку
            else:               print(table[i - 1][j - 1], end=' ')     # Иначе печатаем значение матрицы
        print()


def print_exception(str_exception):
    """Печать комментария на ошибку"""
    if str_exception == 'GivenNotTwoArgs':
        print('Введите координаты корректно, согласно формату')
    elif str_exception == 'CellIsNotEmpty':
        print('Выберите незанятую ячейку')
    elif str_exception == 'OutOfRange':
        print('Выбранные координаты выходят за границу сетки')
    elif str_exception == 'ValueError':
        print('Значение(-я) не является(-ются) числами')
    else:
        print('Произошла непредвиденная ошибка! Попробуйте ещё раз')


def check():
    """Проверка на условие выйгрыша
    Возвращает True, если найден победитель"""
    for i in range(3):
        if ((table[i][0] == table[i][1] == table[i][2] or   # Построчная проверка
            table[0][i] == table[1][i] == table[2][i]) and  # Проверка по столбцам
            table[i][i] != '-'):                            # Проверка на не "пустую" ячейку
            return True
    if ((table[0][0] == table[1][1] == table[2][2] or   # Проверка по главной диагонали
        table[0][2] == table[1][1] == table[2][0]) and # Проверка по побочной диагонали
        table[1][1] != '-'):
        return True

    if turn_count == 9:
        return True

    return False


# ---------------------------------------------------------------------------------------

table = [['-' for _ in range(3)] for _ in range(3)]  # Игровой стол в виде матрицы

turn = True  # Очередь ходящего. True - нолики, False - крестики

turn_count = 0  # Счётчик кол-ва ходов для ничьи

# ---------------------------------------------------------------------------------------

#  Начало тела
while True:
    print_table()
    if turn:
        print('\nСейчас ходят нолики')
    else:
        print('\nСейчас ходят крестики')

    try:
        coords = input('\nВыберите клетку для хода в формате "0 0" (без ковычек), '
                        'где 1-е число - номер строки, а 2-е число - номер столбца: ').split(' ')

        coords = list(map(int, coords))  # Проверка на принадлежность числу

        if len(coords) != 2: raise Exception('GivenNotTwoArgs')  # Проверка на количество элементов

        if not (coords[0] in range(3)
                and coords[1] in range(3)):
            raise Exception('OutOfRange')  # Проверка на выход за границу

        if table[coords[0]][coords[1]] != '-': raise Exception('CellIsNotEmpty')  # Проверка на занятость ячейки

        table[coords[0]][coords[1]] = 'O' if turn else 'X'  # Заполнение ячейки
        turn = not turn  # Переход хода
        turn_count += 1

        if check():
            break
    except Exception as e:
        print_exception(str(e))

win_result = 'Нолики' if not turn else 'Крестики'
print_table()
if turn_count != 9:
    print('Победили %s!' % win_result)
else:
    print('Ничья!')