public void stringSplosionShouldReturn(){
    assert StringSplosion.splode.splode("Code").equals("CCoCodCode");
    assert StringSplosion.splode("abc").equals("aababc");
    assert StringSplosion.splode("ab").equals("aab");
    assert StringSplosion.splode("x").equals("x");
    assert StringSplosion.splode("fade").equals("ffafadfade");
    assert StringSplosion.splode("There").equals("TThTheTherThere");
    assert StringSplosion.splode("Kitten").equals("KKiKitKittKitteKitten");
    assert StringSplosion.splode("Bye").equals("BByBye");
    assert StringSplosion.splode("Good").equals("GGoGooGood");
    assert StringSplosion.splode("Bad").equals("BBaBad");
  }