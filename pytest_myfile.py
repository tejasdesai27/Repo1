from myfile import add_numbers, subtract_numbers, multiply_numbers, divide_numbers


# pass  
def test_add_numbers_pass():     
    assert add_numbers(10, 5) == 15     

# pass 
def test_subtract_numbers_pass():
    assert subtract_numbers(10, 5) == 5  

# pass        
def test_multiply_numbers_pass():
    assert multiply_numbers(10, 5) == 50   
    
     
# fail   
def test_divide_numbers_fail():
    assert divide_numbers(10, 0) == 0  
  
