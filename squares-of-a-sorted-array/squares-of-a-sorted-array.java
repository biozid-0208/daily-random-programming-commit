class Solution {
    public int[] sortedSquares(int[] nums) {
        if(nums.length == 0) return nums;
        int i = 0; 
        int j = nums.length - 1;
        int [] arr = new int[nums.length];
        int idx = nums.length - 1;
        
        while( i <= j){
            if(nums[i]*nums[i] < nums[j]*nums[j]){
                arr[idx] =  nums[j]*nums[j];
                j--;
            }else{
                arr[idx] =  nums[i]*nums[i];
                i++;
            }
            idx--;
                
        }
    return arr;
    }
}