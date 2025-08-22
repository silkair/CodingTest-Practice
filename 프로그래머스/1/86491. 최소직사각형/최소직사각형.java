import java.util.*;

class Solution {
    public int solution(int[][] sizes) {
        
        //가장 긴 변 중 최댓값
        //가장 짧은 변 중 최댓값
        
        int wMax = 0;
        int hMax = 0;
        
        for(int i = 0; i < sizes.length; i++) {
            int w = Math.max(sizes[i][0], sizes[i][1]);
            int h = Math.min(sizes[i][0], sizes[i][1]);
            if(w > wMax) wMax = w;
            if(h > hMax) hMax = h;
        }
        return wMax*hMax;
    }
}