/*
https://leetcode.com/problems/count-primes/
Given an integer n, return the number of prime numbers that are strictly less than n.
 */

package math;

public class CountPrimes {
    public int countPrimes(int n) {
        if (n < 3) {
            return 0;
        }

        int count = 0;
        boolean[] primes = new boolean[n];

        for (int i = 2; i < n; i++) {
            primes[i] = true;
        }

        for (int i = 2; i < Math.sqrt(n); i++) {
            if (primes[i]) {
                for(int j = i * i; j < n; j = j + i) {
                    primes[j] = false;
                }
            }
        }

        for (int i = 2; i < n; i++) {
            if (primes[i]) {
                count++;
            }
        }

        return count;
    }
}
/*
Abordagem: Sieve of Eratosthenes
Ao inves de fazermos na brute force checando de um em um, se eles são primos. Iremos calcular de 1 a n quais os numéros
primos da seguinte forma:
    Se um número é divisel por 2 ele não é primo correto?
    Faremos um array de tamanho [n + 1], e iremos assumir que todos os números a partir do 2 são primos, marcando as
    posições dos números como true ou 1.
    Após isso iremos loopar novamente porém agora de 2 até a raiz de n.
        Checaremos se naquela posição o número é primo. Loopar novamente transformando todos os seus mútiplos em false
        ou 0; => Importante destacar que só precisa começar a partir de i * i. Exemplo: 2x2, 3x3, 5x5.
 */