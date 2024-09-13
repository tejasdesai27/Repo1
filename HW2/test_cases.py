from hw2_debugging import merge_sort


# pass  
def test_case1():     
    assert merge_sort([1,2,6,4]) == [1,2,4,6]     

# pass 
def test_case2():
    assert merge_sort([8,4,7,1]) == [1,4,7,8]  

# pass        
def test_case3():
    assert merge_sort([]) == []   
    