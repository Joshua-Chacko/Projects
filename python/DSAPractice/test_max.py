from MaximumSubArray import *

def test_max_subarray_multiple_cases():
    # Test case 1: Basic case
    assert max_subarray([1, -3, 2, 1, -1], 0, 4) == (2, 3, 3)
    
    # Test case 2: All negative numbers
    assert max_subarray([-2, -3, -1, -5], 0, 3) == (2, 2, -1)
    
    # Test case 3: All positive numbers  
    assert max_subarray([1, 2, 3, 4], 0, 3) == (0, 3, 10)
    
    # Test case 4: Single element
    assert max_subarray([5], 0, 0) == (0, 0, 5)
    
    # Test case 5: Mixed with negative start
    assert max_subarray([-1, 2, 3, -4, 5, 6], 0, 5) == (1, 5, 12)

def test_max_subarray_edge_cases():
    # Single negative element
    assert max_subarray([-5], 0, 0) == (0, 0, -5)
    
    # Two elements
    assert max_subarray([3, -1], 0, 1) == (0, 0, 3)
    assert max_subarray([-1, 3], 0, 1) == (1, 1, 3)
    
    # Classic example from algorithms textbook
    assert max_subarray([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7], 0, 15) == (7, 10, 43)

if __name__ == "__main__":
    # Run tests manually if not using pytest
    test_max_subarray_multiple_cases() 
    test_max_subarray_edge_cases()
    print("All tests passed!")