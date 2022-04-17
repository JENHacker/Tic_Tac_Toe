from random import randint

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
    #turno maquina
    else:
        print("Turno de la maquina\n")
        column = randint(1,l_board)
        row = randint(1,l_board)
        a = 2
    #comprobar
    b = False
    if column > 0 and column <= l_board and row > 0 and row <= l_board and board[row - 1][column - 1] == 0:
        board[row - 1][column - 1] = a
        b = True
        mostrarTablero()
    elif t_plays % 2 == 0:
        print("El valor ingresado no esta permitido, intentelo de nuevo:")
    return b
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
        t_plays += 1
