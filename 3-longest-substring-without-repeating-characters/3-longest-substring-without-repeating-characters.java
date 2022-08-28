class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        int maxL = 0;
        
        for(int i = 0, j = 0; i < s.length(); i++){
           if (map.containsKey(s.charAt(i))){
               j = Math.max(j, map.get(s.charAt(i))+1);
           }
               
            map.put(s.charAt(i),i);
            maxL= Math.max(maxL, i -j +1); 
           
        }
        return maxL;
    }
}