import java.util.*;
//Math.floor(3.14) == 3 :  double 형식으로 저장된다.
class Solution {
    public int solution(int[] wallet, int[] bill) {
        int answer = 0;
        
        if (bill[0]<=wallet[1] && bill[1]<=wallet[0] || bill[0]<=wallet[0] && bill[1]<=wallet[1]){
            return answer;
        } else {
             while ((bill[0]>wallet[0] || bill[0]>wallet[1]) || (bill[1]>wallet[0] || bill[1]>wallet[1])) {
            if (bill[0] >= bill[1]) {
            bill[0] = (int) Math.floor(bill[0]/2);
            answer++;
        } else if (bill[0] < bill[1]) {
            bill[1] = (int) Math.floor(bill[1]/2);
            answer++;
        }
            if ((bill[0]<=wallet[0] && bill[1]<=wallet[1]) || (bill[0]<=wallet[1] && bill[1]<=wallet[0])) {
            break;
                }
            } 
        }    
        return answer;
    }
}