"""
Given a positive integer N., The task is to find the value of Σi from 1 to N F(i) where function F(i) for the number i
is defined as the sum of all divisors of i.
"""


def sumOfDivisors(N):
    sum = 0

    for i in range(1, N + 1):
        sum += int((N // i) * i)

    return sum


"""
Abordagem utilizada:
Primeiro vamos ver um exemplo:
F(1) = 1
F(2) = 1 + 2 = 3
F(3) = 1 + 3 = 4
F(4) = 1 + 2 + 4 = 7
ans = F(1) + F(2) + F(3) + F(4)
    = 1 + 3 + 4 + 7
    = 15

Podemos utilizar a força bruta e ir de número em número e ver seus divisores. Big O(N * sqrt(N))

Ou podemos utilizar a seguinte abordagem, explicarei no exemplo acima:
    Podemos contar quantas vezes 1 aparece nas divisões de 1 a 4 (4 vezes) e, multiplicar pelo seu valor.
    Fazendo isso para todos os números.
    Para aprender o algoritmo pensei da seguinte forma:
        Quantas vezes i cabe em n? Multiplicar o resultado dessa pergunta pelo por i
"""