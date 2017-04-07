### Autor: Yuri Rodrigues
### Matrícula: 15213050337
### Feito em: 27/02/2017
### Descrição: Verifica se um mapa contem um caminho
# para um tesouro.

######	  Fundamentos da Programação	   ######
######		  5ª QUESTÃO				   ######


######	  COMEÇO - FUNÇÕES	   ######
def getMapTreasure():
    map_treasure = []
    return map_treasure


def hasTreasure(path):
    if path == "*":
        return True
    return False


def hasPath():
    return False


######	  TERMINO - FUNÇÕES	   ######


###		Main		###
def main():
    treasure_map = getMapTreasure()
    if hasTreasure(treasure_map):
        if hasPath(treasure_map):
            print("Esse mapa leva ao tesouro")
    else:
        print("Esse mapa não leva a lugar algum")


###		Main		###

main()
