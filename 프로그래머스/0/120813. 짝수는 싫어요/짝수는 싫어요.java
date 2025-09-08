import java.util.*;

class Solution {
    public int[] solution(int n) {

        int k = (n+1)/2;
        int[] arr = new int[k];
        
        for (int i=0; i<k; i++) {
            arr[i] = 2*i+1;
        }
        
        return arr;
    }
}