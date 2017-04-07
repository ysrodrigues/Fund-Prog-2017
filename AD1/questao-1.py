### Autor: Yuri Rodrigues
### Matrícula: 15213050337
### Feito em: 21/02/2017
### Descrição: Programa para ler pares de números(float) do teclado
# ate ser digitado o par (0,0), desconsiderando-o. Como saida o programa
# calculará o ponto médio ou se nenhum ponto for informado além do (0,0)
# escreverá "Não existem pontos!". Separaremos os 2 pontos atraves de um espaço
# ou seja, o ponto (0, 0) na entrada sera 0 0, por exemplo.

######	  Fundamentos da Programação	   ######
######		  1ª QUESTÃO				   ######

######	  COMEÇO - FUNÇÕES	   ######


# Função que retorna uma mensagem caso nenhum par alem do (0,0) for digitado.
def noPair():
    message = "Não existem pontos!"
    return message


# Função para verificar se o par (0,0) foi digitado.
def checkPair(x, y):
    if x == 0 and y == 0:
        return True
    return False


# Função que faz a média entre os pontos.
def media(values):
    sum_values = 0
    # Fator que será dividido os valores para a media; aritimética: (v1 + v2 + v3)/n, onde n é o número de valores somados
    media_factor = len(values)
    for value in values:  # Soma todos os valores
        sum_values += value
    result = float(sum_values / media_factor)
    return result


# Função para retornar apenas 2 casas decimais
def parsingResult(value):
    result = format(value, '.2f')
    return result


# Função para retirada de espaços e transformar os valores em números(float) ao invez de texto(string)
def parsingValues(values):
    result = [float(value) for value in values.split()]
    return result


######	  TERMINO - FUNÇÕES	   ######


###		Main		###
def main():
    getInput = True
    x_values = []
    y_values = []

    while getInput:  # Looping para pegar os valores
        entry = input()
        xy_entry = parsingValues(entry)

        if checkPair(xy_entry[0], xy_entry[1]):  # Verifica parada do looping.
            if not x_values and not y_values:  # Verifica se tem algum valor, legítmo, digitado
                print(noPair())
            else:  # caso tenha faz as médias
                media_x = media(x_values)
                media_y = media(y_values)
                print(parsingResult(media_x), parsingResult(media_y))
            getInput = False  # Termina o looping
        else:
            x_values.append(xy_entry[0])
            y_values.append(xy_entry[1])


###		Main		###

main()
