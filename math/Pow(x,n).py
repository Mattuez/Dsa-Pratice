"""
https://leetcode.com/problems/powx-n/description/
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
"""


def myPow(x, n):
    ans = 1

    if n < 0:
        x = 1 / x
        n = n * -1

    while n > 0:
        if n % 2 != 0:
            ans = ans * x
            n = n - 1
        else:
            x = x * x
            n = int(n / 2)

    return ans


"""
Abordagem utilizada:
    Para ser BigO(log2(n)) é preciso entender duas coisas:
        -> n ** 5 = (n ** 4) * n (Primeiro if)
        -> n**4 = (n ** 2) ** 2 => Dividimos a potencia por dois e multiplicamos n por ele msm. (Segundo if)
        -> n ** 0 = 1 (Condição do loop)
"""