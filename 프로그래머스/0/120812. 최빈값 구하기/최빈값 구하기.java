import java.util.*;

class Solution {
    public int solution(int[] array) {
        int n = array.length;
        int[] max = new int[n];
        
        for(int i = 0; i < n; i++) {
            int count = 0;
            for(int j = 0; j < n; j++) {
                if(array[i] == array[j]) {
                count++;
                }
            }
                max[i] = count;
        }
    
        int best = 0;
        for (int i = 0; i < n; i++) {
            if (max[i] > best) {
                best = max[i];
            }
        }
        
        int mode = -1;
        int RealBest = 0;
        
         for (int i = 0; i < n; i++) {

            boolean first = true;
            
            for (int k = 0; k < i; k++) {
                if (array[k] == array[i]) {
                    first = false;
                    break;
                }
            }
             
            if (!first) continue;

            if (max[i] == best) {
                RealBest++;
                mode = array[i];
                if (RealBest >= 2) return -1;
            }
        }
        return mode;
    }
}