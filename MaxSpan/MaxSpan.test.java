
public void maxSpanShouldReturn(){
    assert maxSpan([1, 2, 1, 1, 3]) == 4;
    assert maxSpan([1, 4, 2, 1, 4, 1, 4]) == 6;
    assert maxSpan([1, 4, 2, 1, 4, 4, 4]) == 6;	
    assert maxSpan([3, 3, 3]) == 3;
    assert maxSpan([3, 9, 3]) == 3;	
    assert maxSpan([3, 9, 9]) == 2;	
    assert maxSpan([3, 9]) == 1;
    assert maxSpan([3, 3]) == 2;	
    assert maxSpan([]) == 0;	
    assert maxSpan([1]) == 1;
}