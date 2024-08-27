class Solution {
    boolean solution(String s) {
        boolean answer = true;

        int pCount = 0;
        int yCount = 0;

        s = s.toLowerCase();
        
        for(int i=0; i<s.length(); i++) {
            if(s.charAt(i)=='p') {
                pCount += 1;
            }
            if(s.charAt(i)=='y') {
                yCount += 1;
            }
        }
        
        if(pCount != yCount) {
            answer = false;
        }

        return answer;
    }
}