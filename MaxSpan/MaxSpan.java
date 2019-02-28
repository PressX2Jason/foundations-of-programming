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