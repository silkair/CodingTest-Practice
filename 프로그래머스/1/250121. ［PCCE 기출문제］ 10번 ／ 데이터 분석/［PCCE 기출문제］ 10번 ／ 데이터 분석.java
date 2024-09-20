import java.util.*;

class Solution {
      
    public int[][] solution(int[][] data, String ext, int val_ext, String sort_by) {
        
        String[] dataArr = {"code", "date", "maximum", "remain"};
        
        int ext_Num = 0;
        int sort_by_Num = 0;
        
        for (int i = 0; i < dataArr.length; i++) {
            if (dataArr[i].equals(ext)) {
                ext_Num = i;
            }
            if (dataArr[i].equals(sort_by)) {
                sort_by_Num = i;
            }
        }

                       
        List<int[]> list = new ArrayList<>();
         for (int[] row : data) {
            if (row[ext_Num] < val_ext) {
                list.add(row);
            }
        }
        
        final int finalSortByNum = sort_by_Num;       
        list.sort(Comparator.comparingInt(row -> row[finalSortByNum]));
        
        int[][] answer = new int[list.size()][data[0].length];
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }
    
        return answer;
    }
}