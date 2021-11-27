###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 15 - Fuga de Nova York II
# Nome: Victor Gabriel Pantaleão Santos
# RA: 248198
###################################################

def acao(lista, x, y):
    if lista[x][y] == 'H': ...
    elif lista[x][y] == 'V': ...
    elif lista[x][y] == 'T': ...
def rota(x, y, lista):
    for i in range(len(lista)*len(lista[0])):
        direcao = lista[x][y]
        if direcao == 'N': return False
        x, y = acao(lista, x, y)
        if x < 0 or x >= len(lista): return True
        elif y < 0 or y >= len(lista[0]): return True
    return True
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
    fuga = rota(x, y, mapa)
