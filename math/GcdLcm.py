"""
https://practice.geeksforgeeks.org/problems/lcm-and-gcd4516/1
Given two numbers A and B. The task is to find out their LCM and GCD. (MMC, MDC)
"""


def lcmAndGcd(a, b):
    def findGcd(first, second):
        while first > 0 and second > 0:
            if second > first:
                aux = first
                first = second
                second = aux
            first = first % second

        return first == 0 and second or first

    gcd = int(findGcd(a, b))
    lcm = a * b // gcd

    return [lcm, gcd]


"""
Abordagem utilizada: findGcd() explicação -> Usaremos o algoritmo de Euclides para achar o mdc.
                         Loopar até o primeiro ou segundo chegar a zero. No looping:
                                O primeiro deve ser sempre o maior, por isso se for ao contrário faremos a troca do 
                                    primeiro pelo segundo.
                                Maior = Maior % menor
                         retorna qual for diferente de zero
                      Para encontrarmos o mmc é uma formula.
"""
