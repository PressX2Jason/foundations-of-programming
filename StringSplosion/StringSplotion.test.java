public void stringSplosionShouldReturn(){
    assert stringSplosion("Code").equals("CCoCodCode");
    assert stringSplosion("abc").equals("aababc");
    assert stringSplosion("ab").equals("aab");
    assert stringSplosion("x").equals("x");
    assert stringSplosion("fade").equals("ffafadfade");
    assert stringSplosion("There").equals("TThTheTherThere");
    assert stringSplosion("Kitten").equals("KKiKitKittKitteKitten");
    assert stringSplosion("Bye").equals("BByBye");
    assert stringSplosion("Good").equals("GGoGooGood");
    assert stringSplosion("Bad").equals("BBaBad");
  }