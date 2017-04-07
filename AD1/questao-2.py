### Autor: Yuri Rodrigues
### Matrícula: 15213050337
### Feito em: 22/02/2017
### Descrição: Programa para verificar quantos e quais pontos estão dentro de um retangulo
# hipotético e quais foram os valores max e min digitados em x e y

######	  Fundamentos da Programação	   ######
######		  2ª QUESTÃO				   ######

######	  COMEÇO - FUNÇÕES	   ######

from sys import maxsize


# Função para retirada de espaços e transformar os valores em números(int) ao invez de texto(string)
def parsingValues(values):
    result = [int(value) for value in values.split()]
    return result


# Função que retorna um array com os maiores valores entre dois array
def max_array_value(array_a=[], array_b=[]):
    result = [
        max_value(value, array_b[index]) for index, value in enumerate(array_a)
    ]
    return result


# Função que retorna um array com os menores valores entre dois array
def min_array_value(array_a=[], array_b=[]):
    result = [
        min_value(value, array_b[index]) for index, value in enumerate(array_a)
    ]
    return result


# Função que retorna quem é o maior entre dois inteiros
def max_value(value_a, value_b):
    if value_a >= value_b:
        return value_a
    else:
        return value_b


# Função que retorna quem é o menor entre dois inteiros
def min_value(value_a, value_b):
    if value_a <= value_b:
        return value_a
    else:
        return value_b


# Função para criar o retangulo a partir dos pontos max e min
def mountRectangle(point_max=[], point_min=[]):
    p_max = []
    for value in point_max:
        p_max.append(value // 2)
    rectangle = [point_min, p_max]
    return rectangle


# Função para verificar se um ponto está dentro de um retângulo
def inRectangle(rec=[[]], p_query=[]):
    largura = min_array_value(rec[0], rec[1])
    altura = max_array_value(rec[0], rec[1])
    if p_query[0] >= largura[0] and p_query[0] <= altura[0] and p_query[1] >= largura[1] and p_query[1] <= altura[1]:
        return True
    return False


# Função para mostrar os resultados
def printResults(max_p=[], min_p=[], points_inside=[[]]):
    print("xMin =", min_p[0], "\nyMin =", min_p[1])
    print("xMax =", max_p[0], "\nyMax =", max_p[1])
    print("Pontos dentro do retângulo:")
    if points_inside:
        for point in points_inside:
            print(point[0], point[1])
    print("Total de Pontos:", len(points_inside))


######	  TERMINO - FUNÇÕES	   ######


###		Main		###
def main():
    max_point = [-maxsize, -maxsize]
    min_point = [maxsize, maxsize]
    points = []
    points_inside = []

    n_points = int(input())

    for n_point in range(n_points):
        entry = input()
        xy_entry = parsingValues(entry)
        points.append(xy_entry)
        max_point = max_array_value(max_point, xy_entry)
        min_point = min_array_value(min_point, xy_entry)

    rec = mountRectangle(max_point, min_point)

    for point in points:
        if inRectangle(rec, point):
            points_inside.append(point)

    printResults(max_point, min_point, points_inside)


###		Main		###

main()
