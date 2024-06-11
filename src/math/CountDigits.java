/*
https://www.geeksforgeeks.org/problems/count-digits5716/1
Given a number N. Count the number of digits in N which evenly divide N.
Note :- Evenly divides means whether N is divisible by a digit i.e. leaves a remainder 0 when divided.
 */
package math;

public class CountDigits {
    public int evenlyDivides(int n) {
        int count = 0;
        int aux = n;

        while (aux > 0) {
            int lastDigit = aux % 10;
            if (lastDigit != 0) {
                if (n % lastDigit == 0) {
                    count++;
                }
            }
            aux = aux / 10;
        }

        return count;
    }
}

/*
Abordagem utilizada:
-> Loopar enquanto o número (n) for maior que zero.
   Dentro do Loop => Pegar o último digito de n atraves de modulo de 10.
                     Se esse número dividir n sem deixar restos aumentar o count.
                     dividir n igual a n dividido por 10 (para retirar o último número)
 */