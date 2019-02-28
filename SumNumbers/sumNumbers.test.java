public void sumNumbershouldReturn(){
    assert sumNumbers("abc123xyz") == 123	
    assert sumNumbers("aa11b33") == 44	
    assert sumNumbers("7 11") == 18	
    assert sumNumbers("Chocolate") == 0	
    assert sumNumbers("5hoco1a1e") == 7	
    assert sumNumbers("5$$1;;1!!") == 7	
    assert sumNumbers("a1234bb11") == 1245	
    assert sumNumbers("") == 0	
    assert sumNumbers("a22bbb3") == 25
}