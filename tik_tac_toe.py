import random

field = [[2,2,2],
         [2,2,2],
         [2,2,2]
]
# Подфункция вывода на экран игрового поля         ]
def field_disp(field):
    line_fild = " "
    for i in field:
        if i==1:
            line_fild = line_fild+" X"
        elif i==0:
            line_fild = line_fild+" 0"
        else:
            line_fild = line_fild+" -"
    return line_fild

# Функция вывода на экран игрового поля
def disp():
    print("   0 1 2")
    print("0"+field_disp(field[0]))
    print("1"+field_disp(field[1]))
    print("2"+field_disp(field[2]))

# Функция ввода координат пользователем
def user_mov(N):
    while True:
        x_str = input("Ваш ход (Введите координаты по горизонтали):")
        y_str = input("Ваш ход (Введите координаты по вертикали):")
        if not(x_str == "0" or x_str == "1" or x_str == "2"):
            print("Введены не корректные координаты! Введите заново")

        elif not(y_str == "0" or y_str == "1" or y_str == "2"):
            print("Введены не корректные координаты! Введите заново")

        else:
            x = int(x_str)
            y = int(y_str)
            temp = field[y]
            if temp[x] == 2:
                temp[x] = N
                field[y] = temp
                break
            else:
                print("Эта ячейка уже занята! Выберите другую")

# Функция выбора случайной клетки компьютером
def ii_mov(N):
    while True:
        x = random.randint (0,2)
        y = random.randint (0,2)
        temp = field[y]
        if temp[x] == 2:
            temp[x] = N
            field[y] = temp
            break

# Подфункция проверки на победу
def line_check(n1,n2,n3,atr_check):
    return  n1 == atr_check and n2 == atr_check and n3 ==atr_check

# Функция проверки на победу
def vic_check(atr_check):
    temp1 = field[0]
    temp2 = field[1]
    temp3 = field[2]
    if line_check(temp1[0],temp2[1],temp3[2],atr_check):
        return True
    elif line_check(temp1[2], temp2[1], temp3[0], atr_check):
        return True
    elif line_check(temp1[0], temp1[1], temp1[2], atr_check):
        return True
    elif line_check(temp2[0], temp2[1], temp2[2], atr_check):
        return True
    elif line_check(temp3[0], temp3[1], temp3[2], atr_check):
        return True
    elif line_check(temp1[2], temp2[2], temp3[2], atr_check):
        return True
    elif line_check(temp1[1], temp2[1], temp3[1], atr_check):
        return True
    elif line_check(temp1[0], temp2[0], temp3[0], atr_check):
        return True
    else:
        return False

# Функция проверки на ничью
def none_check():
    for i in field:
        if 2 in i:
            return False
    return True


if input("Выберите очередность хода (1 - ходить первым):") == "1":
    atr_user, atr_ii = 1, 0
else:
    atr_user, atr_ii = 0, 1


while True:

    if atr_user == 1:
        disp()
        user_mov(atr_user)
        if vic_check(atr_user):
            disp()
            print("Вы выйграли!")
            break

        if none_check():
            print("Ничья")
            disp()
            break
        print("проверка на ничью")

        ii_mov(atr_ii)
        print("Ход компьтера")
        # disp()
        if vic_check(atr_ii):
            disp()
            print("Вы проиграли!")
            break
    else:
        ii_mov(atr_ii)
        print("Ход компьтера")
        disp()
        if vic_check(atr_ii):
            disp()
            print("Вы проиграли!")
            break

        if none_check():
            print("Ничья")
            disp()
            break
        print("проверка на ничью")

        user_mov(atr_user)
        if vic_check(atr_user):
            disp()
            print("Вы выйграли!")
            break



