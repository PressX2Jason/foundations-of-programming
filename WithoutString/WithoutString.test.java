public void withoutStringShouldReturn(){
    assert withoutString("Hello there", "llo").equals("He there");
    assert withoutString("Hello there", "e").equals("Hllo thr");
    assert withoutString("Hello there", "x").equals("Hello there");
    assert withoutString("This is a FISH", "IS").equals("Th a FH");
    assert withoutString("THIS is a FISH", "is").equals("TH a FH");
    assert withoutString("THIS is a FISH", "iS").equals("TH a FH");
    assert withoutString("abxxxxab", "xx").equals("abab");
    assert withoutString("abxxxab", "xx").equals("abxab");
    assert withoutString("abxxxab", "x").equals("abab");
    assert withoutString("xxx", "x").equals("");
    assert withoutString("xxx", "xx").equals("x");
    assert withoutString("xyzzy", "Y").equals("xzz");
    assert withoutString("", "x").equals("");
    assert withoutString("abcabc", "b").equals("acac");
    assert withoutString("AA22bb", "2").equals("AAbb");
    assert withoutString("1111", "1").equals("");
    assert withoutString("1111", "11").equals("");
    assert withoutString("MkjtMkx", "Mk").equals("jtx");
    assert withoutString("Hi HoHo", "Ho").equals("Hi ");
}