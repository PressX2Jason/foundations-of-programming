public void test_sort(){
    assert sort([]) == []
    assert sort([1]) == [1]
    assert sort([1, 1]) == [1]
    assert sort([1, 2]) == [1, 2]
    assert sort([1, 2, 2]) == [1, 2]
    assert sort([1, 2, 3]) == [1, 2, 3]
}