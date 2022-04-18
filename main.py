from random import randint
from traceback import print_tb

winner = False

def mostrarTablero():
    for i in range(l_board + 1):
        print(i,end="   ")
    print("\n")
    for i in range(1,l_board + 1):
        print(i,end="  ")
        for j in range(1,l_board + 1):
            if board[i - 1][j - 1] == 1:
                print(" X ", end="")
            elif board[i - 1][j - 1] == 2:
                print(" O ", end="")
            else:
                print("   ",end="")
            if j < l_board:
                print("|",end="")    
        if i < l_board:
            print("\n   ",end="")
            for j in range(1,l_board * 4):
                print("-",end="")
        print("")
    print("")
    return 

def determinarPosicion():
    #turno jugador
    if t_plays % 2 == 0:
        print("Tu turno\n")
        print("Columna:", end=" ")
        column = int(input())
        print("Fila:", end=" ")
        row = int(input())
        a = 1
        print("")
    #turno maquina
    else:
        column = randint(1,l_board)
        row = randint(1,l_board)
        a = 2
    #comprobar
    b = False
    if column > 0 and column <= l_board and row > 0 and row <= l_board and board[row - 1][column - 1] == 0:
        board[row - 1][column - 1] = a
        b = True
        mostrarTablero()
        comprobarGanador()
    elif t_plays % 2 == 0:
        print("El valor ingresado no esta permitido, intentelo de nuevo:")
    return b

def ganador(num):
    if num == 1:
        print(f"¡Felicidades! {u_name} ha ganado")
    else:
        print("La maquina ha ganado")

def comprobarGanador():
    global winner
    
    #Inicialización variables diagonales.
    i_digit_d1 = board[0][0]
    i_digit_d2 = board[l_board - 1][0]

    p_bool_d1 = True
    p_bool_d2 = True
    for i in range(l_board):
        i_digit_r = board[i][0]        
        i_digit_c = board[0][i]

        p_bool_r = True
        p_bool_c = True
        for j in range(1,l_board):
            a_digit_r = board[i][j] 
            a_digit_c = board[j][i]
            if p_bool_r: 
                p_bool_r = a_digit_r == i_digit_r
            if p_bool_c:
                p_bool_c = a_digit_c == i_digit_c
            if p_bool_c and a_digit_c != 0 or p_bool_r and a_digit_r != 0:
                if j == l_board - 1:
                    ganador((i_digit_r * int(p_bool_r)) + (i_digit_c * int(p_bool_c)))
                    winner = True
            else:
                break
        
        a_digit_d1 = board[i][i]
        a_digit_d2 = board[l_board - 1 - i][i]

        if p_bool_d1:
            p_bool_d1 = i_digit_d1 == a_digit_d1
        if p_bool_d2:
            p_bool_d2 = i_digit_d2 == a_digit_d2
        if p_bool_d1 and a_digit_d1 != 0 or p_bool_d2 and a_digit_d2 != 0:
            if i == l_board - 1:
                ganador((i_digit_d1 * int(p_bool_d1)) + (i_digit_d2 * int(p_bool_d2)))
                winner = True
    return
#Pedir datos antes del juego.
print("¡Hola, nuevo jugador!, estas a punto de jugar al gato, pero antes necesitamos que ingreses algunos datos.\n\nIngrese su nombre de usuario:",end = " ")
u_name = input()

print("\nA continuación ingrese su edad:",end=" ")
u_age = input()

print("\nY por ultimo ingrese un valor para el lado del tablero:",end=" ")
l_board = int(input())
while l_board < 3:
    print("\nValor no permitido, este tiene que ser mayor o igual a 3:",end=" ")
    l_board = int(input())
print("")
#Mostrar tablero
column = 0
row = 0
board = []
for i in range(l_board):
    a = [0] * l_board
    board.append(a)

mostrarTablero()

t_plays = 0
#Juego
while True:
    if determinarPosicion():
        if winner:
            break
        t_plays += 1
        if t_plays % 2 == 1:
            print("Turno de la maquina\n")
print("\ndo you wanna try it again?")