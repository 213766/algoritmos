def isOrdenado(vetor:list[int]):
    copia = vetor.copy()
    copia.sort()
    return copia == vetor

print(isOrdenado([1,2,3,5,4]))