/*
 * https://codingbat.com/prob/p117334
 * Given a non-empty string like "Code" return a string like "CCoCodCode".
 * stringSplosion("Code") → "CCoCodCode"
 * stringSplosion("abc") → "aababc"
 * stringSplosion("ab") → "aab"
 */
  public static String stringSplosion(String str) {
    StringBuilder sb = new StringBuilder();
    for(int i = 1; i < str.length() +1; i++){
      sb.append(str.substring(0, i));
    }
    return sb.toString();
  }

