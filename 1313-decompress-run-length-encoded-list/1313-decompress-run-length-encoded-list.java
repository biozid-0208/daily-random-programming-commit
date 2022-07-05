class Solution {
    public int[] decompressRLElist(int[] nums) {
     int len = 0;  
     for(int i= 0; i < nums.length; i+=2){
        len  += nums[i]; 
     }
        
     int[] res = new int[len];   

     int idx = 0;
     for(int i= 0; i < nums.length; i+=2){
         for(int j = nums[i]; j > 0; j--){
             res[idx] = nums[i+1];
             idx++;
         }
     }
        return res;
    }
}