import java.util.*;

class Solution {
    public int solution(int[] nums) {
        //번호가 키, 빈도가 벨류
        
        Map<Integer,Integer> mon = new HashMap<>();
        
        for (int x : nums) {
            mon.put(x, mon.getOrDefault(x,0) + 1);
        }
        int kinds = mon.size();
        int limits = nums.length / 2;
        
        return Math.min(kinds,limits);
    
    }
}