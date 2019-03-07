/*
 * https://codingbat.com/prob/p262890
 * Return an array that contains the sorted values from the input array with duplicates removed.
 * 
 * 
 * sort([]) → []
 * sort([1]) → [1]
 * sort([1, 1]) → [1]
 */

public int[] sort(int[] a) {
    Set<Integer> set = new HashSet<>();
    for(int i = 0; i < a.length; i++){
      set.add(a[i]);
    }
    int j = 0;
    int[] result = new int[set.size()];
    for(int num : set){
      result[j++] = num;
    }
    return result;
  }
  