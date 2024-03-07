def numberBelongsToFibonacci(numberToBeFound):
    if (numberToBeFound == 0 or numberToBeFound == 1):
        return True
    current = 2
    previous = 1
    #busca até o centésimo número da sequência, mas pode ser alterado para buscar mais
    for i in range(3, 100):
        if (numberToBeFound < current):
           return False
        if (numberToBeFound == current):
           return True
        temp = previous
        previous = current
        current = current + temp 

    return False


n = int(input("Informe o número a ser buscado: "))

if numberBelongsToFibonacci(n):
    print("Número pertence a sequência")
else:
    print("Número não pertence a sequência")