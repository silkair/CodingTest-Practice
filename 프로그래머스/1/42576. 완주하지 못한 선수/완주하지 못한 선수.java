import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> runMap = new HashMap<>();
        
        for(String p : participant) {
            runMap.put(p,runMap.getOrDefault(p,0)+1);
        }
        
        for(String c : completion) {
            runMap.put(c,runMap.get(c)-1);
        }
        
        for(Map.Entry<String,Integer> e : runMap.entrySet()) {
            if (e.getValue() != 0) return e.getKey();
        }
        return "";
    }
}