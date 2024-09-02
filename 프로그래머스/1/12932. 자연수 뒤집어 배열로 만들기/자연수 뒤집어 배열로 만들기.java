class Solution {
    public int[] solution(long n) {
        String str = Long.toString(n);
        int[] answer = new int[str.length()];
   
        for(int i=1; i<str.length()+1; i++) {
            answer[i-1] = str.charAt(str.length()-i) - '0';
        }
        return answer;
    }
}