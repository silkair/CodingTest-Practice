class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] ans = new String[n];
        for (int i = 0; i < n; i++) {
            int row = arr1[i] | arr2[i];
            String bin = Integer.toBinaryString(row);
            String padded = String.format("%" + n + "s", bin);
            ans[i] = padded.replace('1', '#').replace('0', ' ');
        }
        return ans;
    }
}