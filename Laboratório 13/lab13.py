###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Ordenação de Panquecas
# Nome: Victor Gabriel Pantaleão Santos
# RA: 248198
###################################################

panqueca = [int(x) for x in input().split()]
exclude = []
ordenacao = ""
ok = int(0)
for x in range(len(panqueca)):
    maior = None
    for i in panqueca:
        if exclude.count(i) == False:
            if (maior is None or i > maior): maior = i
    exclude.append(maior)
    if panqueca.index(maior) != (len(panqueca) - len(exclude)):
        print("Posicionando a panqueca", maior)
        if panqueca.index(maior) > 0:
            panqueca = panqueca[panqueca.index(maior)::-1]+panqueca[panqueca.index(maior)+1::1]
            for i in panqueca: ordenacao += str(i)+" "
            ordenacao = ordenacao[:len(ordenacao)-1]
            print("Primeira inversao:", ordenacao)
            ordenacao = ""
        if (len(panqueca) - len(exclude) + 1) >= len(panqueca): panqueca = panqueca[len(panqueca) - len(exclude)::-1]
        else: panqueca = panqueca[len(panqueca)-len(exclude)::-1]+panqueca[len(panqueca)-len(exclude)+1::1]
        for i in panqueca: ordenacao += str(i)+" "
        ordenacao = ordenacao[:len(ordenacao)-1]
        print("Segunda inversao:", ordenacao)
        ordenacao = ""
    else: ok += 1
if ok >= len(panqueca): print("Panquecas ja ordenadas")
