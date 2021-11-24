###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - Busca em Imagens
# Nome: Victor Gabriel Pantaleão Santos
# RA: 248198
###################################################

def verify(image):
    # Verify if the image is contained in default image
    for i in range(n_A-len(image) + 1):
        for j in range(m_A-len(image[0]) + 1):
            copy = A[i:i+len(image)]
            aux = []
            for x in range(len(copy)):
                aux.append(copy[x][j:j+len(image[0])])
            # i == 1:
            #    if j == 0:
            #        print(aux, len(image[0]), len(image))
            #        print("i:", i, "j:", j)
            if aux == image: return True
    return False
def flip(image, way):
    # Flip the image and check if it is contained in default image
    aux = []
    if way:
        #print(image)
        for i in range(len(image)):
            image[i].reverse()
        #print(B)
        #print(image)
        if verify(image): return True
        return False
    else: 
        image.reverse()
        #print(B)
        #print(image)
        if verify(image): return True
        return False
def rotation(image, degree):
    # Rotate the image and check if it is contained in default image
    for t in range(int(degree/90)):
        copy = []
        for i in range(len(image[0])):
            aux = []
            for j in range(len(image)):
                aux.append(image[len(image)-j-1][i])
            copy.append(aux)
        image = copy.copy()
    if verify(image): return True
    return False
def result(val):
    if val: return "Contido"
    else: return "Nao contido"
A = []
B = []
A_Format = input()
m_A, n_A = [int(x) for x in input().split()]
size_A = input()
for i in range(n_A):
    l = [int(x) for x in input().split()]
    A.append(l)
B_Format = input()
m_B, n_B = [int(x) for x in input().split()]
size_B = input()
for i in range(n_B):
    l = [int(x) for x in input().split()]
    B.append(l)
#print(B)
print("Original:", result(verify([l.copy() for l in B])))
print("Flip horizontal:", result(flip([l.copy() for l in B], 1)))
print("Flip vertical:", result(flip([l.copy() for l in B], 0)))
print("Rotacao 90:", result(rotation([l.copy() for l in B], 90)))
print("Rotacao 180:", result(rotation([l.copy() for l in B], 180)))
