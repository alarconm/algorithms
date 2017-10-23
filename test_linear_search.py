from linear_search import linear_search

  # Create test methods here
def test_number_in_list():
    assert linear_search(5, (1,2,3,4,5,6,7,8,9,10)) == 4

def test_letter_in_list():
    assert linear_search('e', ['a','b','e','c','d']) == 2

def test_not_in_list():
    assert linear_search(1, (2,3,4,5,6,7,5,4,5)) == -1