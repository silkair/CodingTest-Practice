class Solution {
    public String solution(String phone_number) {
        String answer = "";
        char[] chars = phone_number.toCharArray();
        
        for(int i=0; i<chars.length-4; i++) {
            chars[i] = '*';
        }
        
        answer = String.valueOf(chars);
        return answer;
    }
}