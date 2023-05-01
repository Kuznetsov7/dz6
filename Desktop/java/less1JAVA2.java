import static java.lang.Math.sqrt;


public class less1JAVA2 {
        // Вывести все простые числа от 1 до 1000
        public static void main(String[] args) {
            int start = 1;
            int end = 1000;
            System.out.printf("Prime numbers from %d to %d:\n", start, end);
            for (int i=start; i<=end; i++) {
                if (isPrimeNumber(i)) System.out.println(i);
            }
        }
        public static boolean isPrimeNumber(int number) {
            for (int i=2;i<=(int)sqrt(number);i++) {
                if (number % i == 0) return false;
            }
            return true;
        }
    }


