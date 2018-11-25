import unittest
from vectors import add_vectors,scalar_mult,dot_product

class Tddforvectors(unittest.TestCase):
    

    def test_adding_lists(self):
        self.assertListEqual( [2, 2, 2], add_vectors([1,1,1],[1,1,1]),
        msg='should create a list with corresponding sums of the positional elements of the given vectors')

    
    def test_multiplying_a_vector_with_a_scalar(self):
        self.assertListEqual( [5,10],scalar_mult(5,[1,2]),
        msg= 'should return a list that is a scalar multiple of the first argument' )

    
    def test_vectors_dot_product_method_returns_correct_result(self):
        result = dot_product([1, 2], [1, 4])
        self.assertEqual(9, result)
        
    def test_vectors_add_method_input_is_not_a_string(self):
        self.assertRaises(TypeError, add_vectors, 'two')
 
    def test_vectors_dot_method_input_accepts_a_dictionary(self):
        self.assertRaises(TypeError, add_vectors,{'name':'','addr':''})
    
    def test_vectors_add_method_input_is_not_an_integer(self):
        self.assertRaises(TypeError, add_vectors, 2)

if __name__ == '__main__':
    unittest.main(exit=False)#also can debug using print statements

#Pdp is also awesome

