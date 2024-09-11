field = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

def playing_field(field):
    print("    0   1   2 ")
    for index, row in enumerate(field):
        print(index, "|", " | ".join(row), "|")
        if index == 0 or index == 1:
            print("  |---+---+---|")


def check_winner(field):
    for i in range(3):
        if field[i][0] == field[i][1] == field[i][2] != "-":
            return True
        if field[0][i] == field[1][i] == field[2][i] != "-":
            return True
    
    if field[0][0] == field[1][1] == field[2][2] != "-":
        return True
    if field[0][2] == field[1][1] == field[2][0] != "-":
        return True


current_player = "X"
step = 0

print('Привет! Давай сыграем в игру "Крестики-нолики!"')

while True:
    playing_field(field)
    print(f"Ходит игрок {current_player}.")
    choice_column = int(input("Введите номер столбца (0 - 2): "))
    choice_row = int(input("Введите номер строки (0 - 2): "))

    if field[choice_row][choice_column] != "-":
        print("Клетка уже занята. Выбери другую.")
        continue

    field[choice_row][choice_column] = current_player
    step += 1

    if check_winner(field):
        playing_field(field)
        print(f"Игрок {current_player} выиграл!")
        break

    if step == 9:
        print("Ничья!")
        playing_field(field)
        break

    current_player = "O" if current_player == "X" else "X"
