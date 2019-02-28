/* 
 * https://codingbat.com/prob/p158767
 * Given a non-empty array, 
 * return true if there is a place to split the array 
 * so that the sum of the numbers on one side is equal to the sum of the numbers on the other side.
 * 
 * canBalance([1, 1, 1, 2, 1]) → true
 * canBalance([2, 1, 1, 2, 1]) → false
 * canBalance([10, 10]) → true
 */

public boolean canBalance(int[] nums) {
    int mid = nums.length / 2;
    Boolean moveRight = null;
    while(mid > 0 && mid < nums.length){
        int left = sum(nums, 0, mid);
        int right = sum(nums, mid, nums.length);
      
        if(left == right){
            return true;
        }
        if(moveRight == null){
            if(left > right){
                moveRight = false;
            }else{
                moveRight = true;
            }
        }
        if(moveRight){
            mid += 1;
        }else{
            mid -= 1;
        }
    }
    return false;
  }
  
  private int sum(int[] nums, int start, int end){
    int result = 0;
    for(int i = start; i < end; i++){
      result += nums[i];
    }
    return result;
  }
  