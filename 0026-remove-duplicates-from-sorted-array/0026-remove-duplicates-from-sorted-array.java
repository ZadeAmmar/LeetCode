class Solution {
    public int removeDuplicates(int[] nums) {
        if(nums.length == 0 || nums == null){
            return 0;
        }

        int[] newNums = new int[nums.length];

        int total = 1;
        newNums[0] = nums[0];

        for(int i = 1; i < nums.length; i++){
            if(nums[i] != newNums[total-1]){
                newNums[total] = nums[i];
                nums[total] = newNums[total];
                ++total;
            }
        }

        return total;
    }
}