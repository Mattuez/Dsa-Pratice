"""
https://www.geeksforgeeks.org/problems/count-digits5716/1
Given a number N. Count the number of digits in N which evenly divide N.
Note :- Evenly divides means whether N is divisible by a digit i.e. leaves a remainder 0 when divided.
"""

class Solution:
    def evenlyDivides(self, N):
        count = 0
        aux = N

        while aux > 0:
            lastDigit = aux % 10
            if lastDigit != 0:
                if N % lastDigit == 0:
                    count += 1

            aux = int(aux / 10)

        return count