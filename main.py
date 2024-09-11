map = [1,2,3,
       4,5,6,
       7,8,9]

def print_map():

    print(map[0], end = " ")
    print(map[1], end = " ")
    print(map[2])

    print(map[3], end = " ")
    print(map[4], end = " ")
    print(map[5])

    print(map[6], end = " ")
    print(map[7], end = " ")
    print(map[8])

win =  [[0,1,2],
        [0,3,6],
        [0,4,8],
        [1,4,7],
        [2,5,8],
        [2,4,6],
        [3,4,5],
        [6,7,8]]

def hod_(hod, symbol):
    ind = map.index(hod)
    map[ind] = symbol
def check_res():
    pobeda = ""
    for i in win:
        if map[i[0]] == "X" and map[i[1]] == "X" and map[i[2]] == "X":
            pobeda = "X"
        if map[i[0]] == "0" and map[i[1]] == "0" and map[i[2]] == "0":
            pobeda = "0"
    return pobeda

game_over = False
player = True

while game_over == False:
    print_map()

    if player == True:
        symbol = "X"
        hod = int(input("Человек 1, ваш ход: "))
    else:
        symbol = "O"
        hod = int(input("Человек 2, ваш ход: "))

    hod_(hod, symbol)
    pobeda = check_res()
    if pobeda != "":
        game_over = True
    else:
        game_over = False

    player = not (player)

print_map()
print("Победили", pobeda)