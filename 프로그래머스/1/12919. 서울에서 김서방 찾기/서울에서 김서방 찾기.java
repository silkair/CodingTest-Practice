class Solution {
    public String solution(String[] seoul) {
        int Kim = 0;
        
        for(int i=0; i<seoul.length; i++) {
            if(seoul[i].equals("Kim")) {
                Kim = i;
                break;
            }
        }
        String answer = "김서방은 " + Kim + "에 있다";
        return answer;
    }
}