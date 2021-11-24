###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Cartões de Crédito
# Nome: Victor Gabriel Pantaleão Santos
# RA: 248198
###################################################

# Leitura de dados
score     = int (input())
idade     = int (input())
saldo     = float (input())
salario   = float (input())
resultado = True

# Verificação se o cartão de crédito será concedido ou não
if score>=300:
    if score<600:
        if idade<30:
            resultado = not resultado
        else:
            if salario<3000:
                resultado = not resultado
            else:
                if (saldo<7000):
                    resultado = not resultado
    else:
        if idade<50:
            if salario<2000:
                if saldo<5000:
                    resultado = not resultado
else:
    resultado = not resultado

#Resultado da consulta
if resultado:
    print ("Cartao concedido")
else:
    print ("Cartao nao concedido")
