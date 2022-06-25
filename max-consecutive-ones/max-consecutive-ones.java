class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
       int i = 0 ;
       int max_count = 0;
       for(int k =0; k < nums.length; k++){
       if(nums[k] == 1)
           i++;
        else{
            max_count = Math.max(i, max_count);
            i = 0;
        }
       }
         
        
        return Math.max(i, max_count);
    }
}