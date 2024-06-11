/*
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
https://leetcode.com/problems/powx-n/description/
 */

package math;

public class MyPow {
    public double myPow(double x, int n) {
        double ans = 1;
        double aux = x;

        if (n == 0) {
            return 1;
        }
        if (n < 0) {
            n = n * -1;
            aux = 1 / aux;
        }

        while (n > 0) {
            if (n % 2 != 0) {
                n--;
                ans = ans * aux;
            } else {
                aux = aux * aux;
                n = n /2;
            }
        }

        return ans;
    }
}

/*
Abordagem utilizada:
    Para ser BigO(log2(n)) é preciso entender duas coisas:
        -> n ** 5 = (n ** 4) * n (Primeiro if)
        -> n**4 = (n ** 2) ** 2 => Dividimos a potencia por dois e multiplicamos n por ele msm. (Segundo if)
        -> n ** 0 = 1 (Condição do loop)
 */