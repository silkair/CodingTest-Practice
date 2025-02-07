import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int N = scanner.nextInt();
        
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = scanner.nextInt();
        }
        
        int M = arr[0];
        for (int i = 1; i < N; i++) {
            if (arr[i] > M) {
                M = arr[i];
            }
        }
        
        double total = 0;
        for (int i = 0; i < N; i++) {
            total += (arr[i] / (double) M) * 100;
        }
        
        double result = total / N;
        System.out.printf("%.6f\n", result);
        
        scanner.close();
    }
}
