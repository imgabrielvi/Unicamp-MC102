###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Avatar
# Nome: Victor Gabriel Pantaleão Santos
# RA: 248198
###################################################

# Inicialização das variáveis
elemento = chr(0)
p        = int(0)
x        = bool(1)
water    = int(0)
earth    = int(0)
fire     = int(0)
air      = int(0)

# Leitura da sequência de treinamento
while x:
    elemento = str(input())
    if elemento == 'X':
        x = 0
        break
    p = int(input())
    if elemento == 'W':
        water = p + water
        if fire < p/2: fire = 0
        else: fire = -p/2 + fire
    if elemento == 'E':
        earth = p + earth
        if air < p/2: air = 0
        else: air = -p/2 + air
    if elemento == 'F':
        fire = p + fire
        if water < p/2: water = 0
        else: water = -p/2 + water
    if elemento == 'A':
        air = air + p
        if earth < p/2: earth = 0
        else: earth = -p/2 + earth

# Impressão das informações de saída
print("Pontuacao Final")
print("Agua: {:.1f}".format(water))
print("Terra: {:.1f}".format(earth))
print("Fogo: {:.1f}".format(fire))
print("Ar: {:.1f}".format(air))
if water:
    if earth:
        if fire:
            if air:
                print("Treinamento realizado com sucesso.")
            else:
                print("Realize mais treinamentos.")
        else:
            print("Realize mais treinamentos.")
    else:
        print("Realize mais treinamentos.")
else:
    print("Realize mais treinamentos.")
