public void testInterpret(){
    assert interpret(1, ["+"], [1]) == 2;
    assert interpret(4, ["-"], [2]) == 2;
    assert interpret(1, ["+", "*"], [1, 3]) == 6;
    assert interpret(3, ["*"], [4]) == 12;
    assert interpret(0, ["?"], [4]) == -1;
    assert interpret(1, ["+", "*", "-"], [1, 3, 2]) == 4;
}