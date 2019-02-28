public void canBalanceShouldReturn(){
    assert canBalance([1, 1, 1, 2, 1]) == true		
    assert canBalance([2, 1, 1, 2, 1]) == false		
    assert canBalance([10, 10]) == true		
    assert canBalance([10, 0, 1, -1, 10]) == true		
    assert canBalance([1, 1, 1, 1, 4]) == true		
    assert canBalance([2, 1, 1, 1, 4]) == false		
    assert canBalance([2, 3, 4, 1, 2]) == false		
    assert canBalance([1, 2, 3, 1, 0, 2, 3]) == true		
    assert canBalance([1, 2, 3, 1, 0, 1, 3]) == false		
    assert canBalance([1]) == false		
    assert canBalance([1, 1, 1, 2, 1]) == true	
}