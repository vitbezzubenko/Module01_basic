from sorting import bubble
from wall import main


def menu():
    print('Данная программа, выполняет четыре действия: ')
    print('1 - сортировка чисел методом "пузырька')
    print('2 - печать результата кирпичной стены')
    print('3 - работа с ключами, из списка словарей')
    print('q - выход из программы')


while True:
    menu()
    user_input = input()
    if user_input == '1':
        print('Введите данные для сортировки, через пробел: ')
        sort = list(map(int, input().split()))
        print('Начальный список > ''\n', sort)
        sort = bubble(sort)
        print('Список, после сортировки > ''\n', bubble(sort))
        continue

    elif user_input == '2':
        main()

    elif user_input == '3':
        print('В программу, загружен стандартный словарь. Вам необходимо ввести значения  keys, '
              'по которым он будет отобран!')
        data = [
            {'Имя': 'Маша', 'Фамилия': 'Иванова', 'Возраст': 28},
            {'Имя': 'Маша', 'Фамилия': 'Иванова', 'Возраст': 27},
            {'Имя': 'Маша', 'Фамилия': 'Петрова', 'Возраст': 27},
            {'Имя': 'Маша', 'Фамилия': 'Cидорова', 'Возраст': 27}
        ]
        print(data)
        keys = input('Введите или скопируйте необходимы keys...  ')
        unig = []
        result = []
        for _dict in data:
            for key in _dict:
                if key in keys:
                    if _dict[key] not in unig:
                        unig.append(_dict[key])
                        result.append(_dict)

        print(result)
    elif user_input == 'q':
        print('Выполние программы завершено. Пока!')
        break
    else:
        print('Неправильный ввод! Выберите одно из предложенных значений (1, 2, 3, q) и повторите ввод!')
