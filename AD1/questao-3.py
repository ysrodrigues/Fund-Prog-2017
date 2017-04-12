### Autor: Yuri Rodrigues
### Matrícula: 15213050337
### Feito em: 23/02/2017
### Descrição: Cria uma matriz bidimensional, onde  o tamanho da matriz é
# dado pelo usuário, com números aleatórios de 10 a 99
# e cria submatrizes 3x3, se existirem, onde todos os valores ao seu lado
# são maiores que ele.

######	  Fundamentos da Programação	   ######
######		  3ª QUESTÃO				   ######

from random import randint

######	  COMEÇO - FUNÇÕES	   ######


# Função para retirada de espaços e transformar os valores em números(float) ao invez de texto(string)
def parsingValues(values=0):
    result = [int(value) for value in values.split()]
    return result


# Função para criar uma matrix[linha][colunas] com números randomicos de 10 a 99 dentro
def createRandomMatrix(lines=0, columns=0):
    matrix = [[randint(10, 99) for c in range(columns)] for l in range(lines)]
    return matrix


#Função que retira uma submatrix 3x3 apartir da linha e coluna dada.
def createMatrix3(m, l, c):
    matrix = [[m[l - 1][c - 1], m[l - 1][c],
               m[l - 1][c + 1]], [m[l][c - 1], m[l][c], m[l][c + 1]],
              [m[l + 1][c + 1], m[l + 1][c], m[l + 1][c + 1]]]
    return matrix


# Função que verifica se tem alguma matrix 3x3 dentro da matrix dada, onde o valor central é menor que todos ao seu redor
def getMatrixMiddle(matrix):
    if len(matrix) >= 3:  # Se a matrix for menor que a 3x3 não faz nd
        maxline = len(matrix) - 1
        maxcolumn = len(matrix[0]) - 1
        line = 1
        while line < len(
                matrix
        ) - 1:  # Varre a matrix da linha 1 ate o l-1 linhas, onde l = total de linhas
            column = 1
            while column < maxcolumn:  # Varre a matrix da coluna 1 ate a c-1 colunas, onde c = total de colunas
                value = matrix[line][column]
                if value < matrix[line][column +
                                        1]:  # Verifica se o valor a frente é menor
                    if value < matrix[line -
                                      1][column] and value < matrix[line +
                                                                    1][column]:  # Verifica os valores na horizontal
                        if value < matrix[line -
                                          1][column -
                                             1] and value < matrix[line +
                                                                   1][column -
                                                                      1]:  # Verifica os valores na diagonal
                            if value < matrix[line -
                                              1][column +
                                                 1] and value < matrix[line +
                                                                       1][column
                                                                          +
                                                                          1]:  # Verifica os valores na diagonal
                                if column == 1:  # Verifica se o valor a atras é menor, caso seja coluna 1
                                    if value < matrix[line][column - 1]:
                                        matrix_3x3 = createMatrix3(
                                            matrix, line, column)
                                        printMatrix(matrix_3x3)
                                        print()
                                else:
                                    matrix_3x3 = createMatrix3(
                                        matrix, line, column)
                                    printMatrix(matrix_3x3)
                                    print()
                    column += 2  # Caso não encontre o valor pula 2 linhas, pois o proxima valor já não é válido pois v+1 > v, v = valor
                else:  # Caso não seja menor pula pro da frente
                    column += 1
            line += 1


def printMatrix(
        matrix):  # Função que imprime na tela de forma convencional uma matrix
    for l in matrix:
        for c in l:
            print(c, end=" ")
        print()


######	  TERMINO - FUNÇÕES	   ######


###		Main		###
def main():
    entry = input()
    lc_matrix = parsingValues(entry)
    valores = createRandomMatrix(lc_matrix[0], lc_matrix[1])
    printMatrix(valores)
    print()
    getMatrixMiddle(valores)


###		Main		###

main()
