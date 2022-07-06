class Solution {
    public int balancedStringSplit(String s) {
        int countOfL = 0;
        int countOfSplit = 0;
        
        for(int i = 0 ; i < s.length() ; i++){
            
            countOfL += s.charAt(i) == 'L' ? 1 : -1;
            if(countOfL == 0) countOfSplit++;
        }
        return countOfSplit;
    }
}