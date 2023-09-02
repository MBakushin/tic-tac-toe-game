player_1 = 'x'  # x
player_2 = '0'  # 0

net = [['-' for i in range(3)] for i in range(3)]


def greet():
    multiline_output = """\nПриветствуем в игре крестики-нолики!
Формат ввода - два символа через пробел, 
первый символ - выбор по диагонали,
второй символ - выбор по вертикали. 
Пример: 0 0
Удачи в игре!\n"""
    print(multiline_output)


def gen_turn():
    for i in range(1, 10):
        if i % 2 == 0:
            yield player_2
        else:
            yield player_1


def input_sym(player):
    available_sym = ['0', '1', '2']
    cell = input(f'{player} ходит: ').split(' ')

    if len(cell) != 2:
        print('Введите два символа!')
        return input_sym(player)

    for i in range(2):
        if cell[i] not in available_sym:
            print('Выберите из доступных символов!')
            return input_sym(player)

        cell[i] = int(cell[i])

    if net[cell[0]][cell[1]] != '-':
        print('Выберите незанятую клетку!')
        return input_sym(player)

    net[cell[0]][cell[1]] = player


def check_win(player):
    win_list = [player for i in range(len(net))]

    for i in net:  # horizontal win
        if i == win_list:
            print(f'{player} выиграл!')
            exit()

    for i in range(len(net)):  # vertical win
        symbols = []
        for j in range(len(net)):
            symbols.append(net[j][i])
        if symbols == win_list:
            print(f'{player} выиграл!')
            exit()

    def check_win_diagonal():
        right_diagonal = []
        left_diagonal = []
        diagonal_tuple = (right_diagonal, left_diagonal)
        for i in range(len(net)):
            right_diagonal.append(net[i][i])
            left_diagonal.append(net[i][-i-1])
        if win_list in diagonal_tuple:
            print(f'{player} выиграл!')
            exit()
            
    check_win_diagonal()


def net_output():
    print('     0 | 1 | 2')
    for index, num in enumerate(net):
        row = ' | '.join(num)
        print(' - - - - - - - ')
        print(f' {index} | {row}')
    print()


greet()
net_output()
for i in gen_turn():
    input_sym(i)
    net_output()
    check_win(i)
print('Ничья!')
