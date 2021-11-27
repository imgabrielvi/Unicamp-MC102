###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 15 - Fuga de Nova York II
# Nome: Victor Gabriel Pantaleão Santos
# RA: 248198
###################################################

def acao(lista, x, y):
    if lista[x][y] == 'H':
        if y > (len(lista[x]) - 1 - y): return (x, y + 1)
        return (x, y - 1)
    elif lista[x][y] == 'V':
        if x > (len(lista) - 1 - x): return (x + 1, y)
        return (x - 1, y)
    elif lista[x][y] == 'T': 
        if x > y:
            if y > (len(lista) - 1 - x): return (x + 1, y)
            return (x, y - 1)
        if x > (len(lista[x]) - 1 - y): return (x, y + 1)
        return (x - 1, y)
def rota(x, y, lista):
    for i in range(len(lista)*len(lista[0])):
        direcao = lista[x][y]
        if direcao == 'N': return "Resgate aereo solicitado."
        x, y = acao(lista, x, y)
        if x < 0 or x >= len(lista): return "Fuga da cidade realizada."
        elif y < 0 or y >= len(lista[0]): return "Fuga da cidade realizada."
    return "Resgate aereo solicitado."
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
