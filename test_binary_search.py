from binary_search import binary_search

class TestBinarySearch(object):
    
    def test_number_sorted_list(self):
        assert binary_search(3, [1,2,3,4,5,6,7,8],0,None) == 2

    def test_number_not_in_list(self):
        assert binary_search(3, [1,2,4,5,6,7,8,9],0,None) == -1

    def test_not_a_number(self):
        assert binary_search('e', [1,2,3,4,5,6,7,8,9,10],0,None) == 'NaN'

    def test_list_size_of_two(self):
        assert binary_search(3, [1,3],0,None) == 1

    def test_negative_number(self):
        assert binary_search(-3,[-5,-4,-3,-2,-1,0,1],0,None) == 2

    def test_unsorted_list(self):
        assert binary_search(3, [1,5,7,9,11,16,2,3],0,None) == 2

    


