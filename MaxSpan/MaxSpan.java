/*
 * https://codingbat.com/prob/p189576
 * Consider the leftmost and righmost appearances of some value in an array. We'll say that the "span" is the number of elements between the two inclusive. A single value has a span of 1. Returns the largest span found in the given array. (Efficiency is not a priority.)
 * maxSpan([1, 2, 1, 1, 3]) → 4
 * maxSpan([1, 4, 2, 1, 4, 1, 4]) → 6
 * maxSpan([1, 4, 2, 1, 4, 4, 4]) → 6
 */
public int maxSpan(int[] nums) {
    HashMap<Integer, Integer> positionMap = new HashMap<>();
    int maxSpan = 0;
    for(int i = 0; i < nums.length; i++){
      if(!positionMap.containsKey(nums[i])){
        positionMap.put(nums[i], i);
        continue;
      }
      
      int span = i - positionMap.get(nums[i]) + 1;
      if (span > maxSpan){
        maxSpan = span;
      }
    }
    
    if(maxSpan == 0 && positionMap.size() > 0){
      maxSpan = 1;
    }
    
    return maxSpan;
  }