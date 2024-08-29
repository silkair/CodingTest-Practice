class Solution {
    public long[] solution(int x, int n) {
        long[] answer = new long[n]; //타입[] 변수 = new 타입[길이]

        for(int i=0; i<n; i++) {
            answer[i] = (long)x + ((long)x*i);
        }
        
        return answer;
    }
}