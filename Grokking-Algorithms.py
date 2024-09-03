from collections import deque

# some simple functions with recursion
def soma(arr: list):
    if arr == []:
        return 0

    return arr[0] + soma(arr[1:])


def conta(arr: list):
    if arr == []:
        return 0

    return 1 + conta(arr[1:])


def maior_valor(arr: list):
    if len(arr) == 2:
        if arr[0] > arr[1]:
            return arr[0]
        else:
            return arr[1]

    sub_maior = maior_valor(arr[1:])
    return arr[0] if arr[0] > sub_maior else sub_maior

# implementation suggested by the author
def binary_search(arr, item):
    high = len(arr) - 1
    floor = 0

    while floor <= high:
        mid = round((high+floor) / 2)
        if arr[mid] == item:
            return mid
        if item > arr[mid]:
            floor = mid + 1
        else:
            high = mid - 1

# implementing recursion to the algorithm
def recursive_binary_search(array, item, floor=0, high=None):
    if high is None:
        high = len(array) - 1
    if floor > high:
        return False

    mid = (high+floor) // 2

    if array[mid] == item:
        return mid

    if item > array[mid]:
        return recursive_binary_search(array, item, mid+1, high)
    else:
        return recursive_binary_search(array, item, floor, mid-1)

# implementation suggested by the author
def quicksort(lista):
    if len(lista) < 2:
        return lista

    pivo = lista[0]
    bigger = [number for number in lista[1:] if number >= pivo]
    lower = [number for number in lista[1:] if number < pivo]

    return quicksort(lower) + [pivo] + quicksort(bigger)

# an alternative with less memory usage
def better_quicksort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left < right:
        pi = partition(arr, left, right)
        better_quicksort(arr, pi+1, right)
        better_quicksort(arr, left, pi-1)


def partition(arr, left, right):
    pivot = arr[right]

    i = left - 1

    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[right] = arr[right], arr[i+1]

    return i+1


def pessoa_e_vendedor(pessoa):
    if pessoa[-1] == 'm':
        return True
    return False

# defining the graph as the author suggests
grafo = {}

grafo['voce'] = ['alice', 'bob', 'claire']
grafo['bob'] = ['anuj', 'peggy']
grafo['alice'] = ['peggy', 'voce']
grafo['claire'] = ['thom', 'jonny']
grafo['anuj'] = []
grafo['peggy'] = []
grafo['thom'] = []
grafo['jonny'] = []

# Breadth-First Search (BFS), in Portuguese for now...
def pesquisa_em_largura(nome):
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo[nome]
    verificadas = []
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if pessoa not in verificadas:
            if pessoa_e_vendedor(pessoa):
                print(f'{pessoa} é um vendedor!')
                return True
            else:
                fila_de_pesquisa += grafo[pessoa]
                verificadas.append(pessoa)
    return False


pesquisa_em_largura('voce')

# completely manual configuration, for now, of a new graph
grafo2: dict = {
    'a': {'b': 2, 'c': 6},
    'b': {'d': 7},
    'c': {'d': 2, 'e': 10},
    'd': {'e': 2},
    'e': {},
}

custos = {
    'b': 2,
    'c': 6,
    'd': float("inf"),
    'e': float("inf"),
}

pais = {
    'b': 'a',
    'c': 'a',
}
analisados: list = []

# take the direction with the lowest cost, also in Portuguese for now
def pega_menor_caminho(custos: dict, analisados):
    menor_valor = float('inf')
    nodo_com_menor_custo = None
    for nodo, custo in custos.items():
        if custo < menor_valor and nodo not in analisados:
            menor_valor = custo
            nodo_com_menor_custo = nodo

    return nodo_com_menor_custo

# a somewhat improvised implementation of the dijkstra algorithm, also being worked on for a better version
def dijkstra_algoritim(grafo, custos, pais, analisados):
    nodo = pega_menor_caminho(custos, analisados)
    while nodo is not None:
        custo = custos[nodo]
        vizinhos: dict = grafo[nodo]
        for k, v in vizinhos.items():
            novo_custo = custo + v
            if novo_custo < custos[k]:
                custos[k] = novo_custo
                pais[k] = nodo
        analisados.append(nodo)
        nodo = pega_menor_caminho(custos, analisados)

# function to show the results
def print_caminho(pais, custofinal, custos):
    for k, v in pais.items():
        print(f'{v} -> {k} | {custos[k]}')
    print(f'custo total a -> {k}: {custofinal}')


dijkstra_algoritim(grafo2, custos, pais, analisados)
print_caminho(pais, custos["e"], custos)

# just some manual testing for now
print('-'*40)

grafo3: dict = {
    'a': {'b': 5, 'c': 2},
    'b': {'d': 4, 'e': 2},
    'c': {'b': 8, 'e': 7},
    'd': {'e': 6, 'f': 3},
    'e': {'f': 1},
    'f': {},
}

custos2 = {
    'b': 5,
    'c': 2,
    'd': float("inf"),
    'e': float("inf"),
    'f': float("inf")
}

pais2 = {
    'b': 'a',
    'c': 'a',
}
analisados2: list = []

dijkstra_algoritim(grafo3, custos2, pais2, analisados2)
print_caminho(pais2, custos2["f"], custos2)

# more tests
print('-'*40)

grafo4: dict = {
    'a': {'b': 10},
    'b': {'c': 20, },
    'c': {'d': 1, 'e': 30},
    'd': {'b': 1},
    'e': {},
}

custos3 = {
    'b': 10,
    'c': float('inf'),
    'd': float("inf"),
    'e': float("inf"),
}

pais3 = {
    'b': 'a',
}
analisados3: list = []

dijkstra_algoritim(grafo4, custos3, pais3, analisados3)
print_caminho(pais3, custos3["e"], custos3)
