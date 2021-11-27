###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 15 - Fuga de Nova York II
# Nome: Victor Gabriel Pantaleão Santos
# RA: 248198
###################################################

def acao(lista, x, y):
    global way
    if lista[x][y] == 'H':
        if y > (len(lista[x]) - 1 - y):
            if y+way < len(lista[x]):
                if lista[x][y+way] == 'N': way = way*(-1) 
            return (x, y + way)
        else:
            if y-way:
                if lista[x][y-way] == 'N': way = way*(-1)
            return (x, y - 1)
    elif lista[x][y] == 'V':
        if x > (len(lista) - 1 - x):
            if x+way < len(lista):
                if lista[x+way][y] == 'N': way = way*(-1)
            return (x + way, y)
        else:
            if x-way:
                if lista[x-way][y] == 'N': way = way*(-1)
            return (x - way, y)
    elif lista[x][y] == 'T': 
        if x > y:
            if y > (len(lista) - 1 - x):
                if x+way < len(lista) and lista[x+way][y] == 'N':
                    if y-way and lista[x][y-way] == 'N':
                        way = way*(-1)
                    return (x, y-way)
                return (x + way, y)
            else:
                if y-way:
                    if lista[x][y-way] == 'N': way = way*(-1)
                return (x, y - way)
        if x > (len(lista[x]) - 1 - y):
            if y+way < len(lista[x]):
                if lista[x][y+way] == 'N': way = way*(-1)
            return (x, y + way)
        else:
            if x-way:
                if lista[x-way][y] == 'N': way = way*(-1)
            return (x - way, y)
    return (x, y)
def rota(x, y, lista):
    if lista[x][y] == 'N': return "Resgate aereo solicitado."
    for i in range(len(lista)*len(lista[0])):
        x, y = acao(lista, x, y)
        if x < 0 or x >= len(lista): return "Fuga da cidade realizada."
        elif y < 0 or y >= len(lista[0]): return "Fuga da cidade realizada."
    return "Resgate aereo solicitado."
way = int(-1)
mapa = []
equipe = []
l = input()
while not(l.isnumeric()):
    mapa.append(l.split())
    l = input()
for i in range(int(l)): equipe.append(input().split())
for i in range(len(equipe)):
    x = int(equipe[i][0])
    y = int(equipe[i][1])
    print(rota(x, y, mapa))
    way = -1
