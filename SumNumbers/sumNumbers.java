/*
 * https://codingbat.com/prob/p121193
 * Given a string, return the sum of the numbers appearing in the string, ignoring all other characters.
 * A number is a series of 1 or more digit chars in a row. 
 * (Note: Character.isDigit(char) tests if a char is one of the chars '0', '1', .. '9'. Integer.parseInt(string) converts a string to an int.)
 * 
 * sumNumbers("abc123xyz") → 123
 * sumNumbers("aa11b33") → 44
 * sumNumbers("7 11") → 18
 */ 

public int sumNumbers(String str) {
    int total = 0;
    for(int i = 0; i < str.length(); i++){
      char c = str.charAt(i);
      if (!Character.isDigit(c)){
        continue;
      }
      int start = i;
      while(i < str.length() && Character.isDigit(str.charAt(i))){
        i++;
      }
      int end = i;
      int num = Integer.parseInt(str.substring(start,end));
      total += num;
    }
    return total;
}
  