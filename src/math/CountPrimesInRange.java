/*
Given two numbers L and R(L<R). Count all the prime numbers in the range [L, R].
https://www.geeksforgeeks.org/problems/count-primes-in-range1604/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article
 */


package math;

public class CountPrimesInRange {
    public int countPrimes(int L, int R) {
        int[] primes = new int[R + 1];
        int count = 0;

        for (int i = 2; i <= R; i++) {
            primes[i] = 1;
        }

        for (int i = 2; i <= Math.sqrt(R); i++) {
            if (primes[i] == 1) {
                for (int j = i * i; j <= R; j = j + i) {
                    primes[j] = 0;
                }
            }
        }

        for (int i = 2; i < R; i++) {
            count = count + primes[i];
            primes[i] = count;
        }

        return primes[R] - primes[L - 1];
    }
}

/*
Abordagem: Sieves of Eratosthenes.
Ir ao problema: "CountPrimes"
Após computar os números primos. Ler novamente o array, dessa vez substituindo se é primo ou não pelo count.
count = count + primes[i]
retornar os números primos até R - os números primos antes de L.
 */