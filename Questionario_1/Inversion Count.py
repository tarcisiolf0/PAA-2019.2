inversoes = 0

def Simple_Merge(list_a, list_b):
    global inversoes
    total = len(list_a) + len(list_b)
    j = k = 0
    list_c = list()

    for i in range(total):

        if (k == len(list_b) or ((j < len(list_a)) and (list_a[j] <= list_b[k]))):
            list_c.append(list_a[j])
            j += 1

        else:
            list_c.append(list_b[k])
            k += 1
            inversoes += (len(list_a) - j)

    return list_c

def Merge_Sort(vetor):

    if (len(vetor) <= 1):
        return(vetor)

    meio = int(len(vetor) // 2)

    esquerda = Merge_Sort(vetor[0 : meio])
    direita = Merge_Sort(vetor[meio : len(vetor)])
    resultado = Simple_Merge(esquerda, direita)

    return resultado

#Teste
casos = int(input())

for i in range(casos):
    input()
    list_a = list()
    tamanho = int(input())
    for j in range(tamanho):
        aux = int(input())
        list_a.append(aux)
    Merge_Sort(list_a)
    print(inversoes)
    inversoes = 0