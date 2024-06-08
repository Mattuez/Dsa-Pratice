"""
https://www.geeksforgeeks.org/problems/largest-prime-factor2601/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article
Given a number N, the task is to find the largest prime factor of that number.
"""


def largestPrimeFactor(n):
    primeNumber = 2

    for i in range(2, int(n ** (1 / 2) + 1)):
        if n % i == 0:
            primeNumber = i

            while n % i == 0:
                n = int(n / i)

    return n != 1 and n or primeNumber


"""
Abordagem utilizada:
Meu primeiro pensamento foi loopar enquanto n != 1 e criar uma variavel i que seria incrementada toda vez que o 
loop fosse executado:
    Dentro do loop iriamos ver se i dividiria n com resto zero, caso dividisse iriamos dividir até não ser mais 
        divisivel e atribuir i ao numero primo mais alto.
    BigO(N) => Pois se o numero for primo, iriamos ter que ir até ele.
Porem é possivel fazer em BigO(sqrt(n)):
    Iremos loopar até a raiz quadrada de N:
        Ver se n é dividido por i, caso seja dividir até não poder mais e o numero primo é i.
    No retorno iremos checar se n é igual a 1, retornamos o número primo, caso não retornamos n
"""