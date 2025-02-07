import java.util.*;

public class Main{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int[] arr = new int[42];
        int count = 0;
        
        for (int i=0; i < 10; i++) {
            int n = scanner.nextInt();
            int k = n%42;
            
            if (arr[k] == 0) {
                arr[k] = 1;
                count++;
            }
        }
        
        scanner.close();
        
        System.out.println(count);
    }
}