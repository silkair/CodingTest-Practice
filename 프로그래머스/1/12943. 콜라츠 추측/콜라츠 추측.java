class Solution {
    public int solution(long num) {
        int answer = 0;
        
        for(int i = 0; i<500; i++) {
            if(num == 1)
                break;
              
            if(num%2 == 0) {
               num = num/2;
           }
            else
                num = num*3 + 1;
            answer = i+1;
        }
        
        if(num != 1)
            answer = -1;
            
        return answer;
    }
}