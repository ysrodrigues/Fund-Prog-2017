### Autor: Yuri Rodrigues
### Matrícula: 15213050337
### Feito em: //2017
### Descrição: Verifica se um número é perfeito ou não.

######	  Fundamentos da Programação	   ######
######		  4ª QUESTÃO				   ######

######	  COMEÇO - FUNÇÕES	   ######


# Função que verifica se o número e perfeito
def isPerfect(number=1):
    all_divisors = getDivisors(number)
    sum_divisors = 0
    for divisor in all_divisors:
        sum_divisors += divisor
    if sum_divisors == number:
        return True
    return False


# Função que retorna todos os divisores de um número
def getDivisors(number=1):
    divisors = []
    d = 1
    while d < number:
        if number % d == 0:
            divisors.append(d)
        d += 1
    return divisors


######	  TERMINO - FUNÇÕES	   ######


###		Main		###
def main():
    queries = []
    cases = int(input())
    for case in range(cases):
        q = int(input())
        queries.append(q)
    for query in queries:
        if isPerfect(query):
            print(query, "é perfeito")
        else:
            print(query, "não é perfeito")


###		Main		###

main()
