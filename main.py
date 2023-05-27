table = [['-' for _ in range(3)] for _ in range(3)]  # Игровой стол в виде матрицы

turn = True  # Очередь ходящего. True - нолики, False - крестики

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
    pass


#  Начало тела
while True:
    print_table()
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

        if check():
            break
    except Exception as e:
        print_exception(str(e))