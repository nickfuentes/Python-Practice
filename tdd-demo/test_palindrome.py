import unittest 
from palindrome import Palindrome

class PalindromeTestCase(unittest.TestCase): 

     # fired BEFORE running each test
    def setUp(self): 
        print("SETUP")
        self.palindrome = Palindrome("344")

    # Make sure your test functions start with test_
    def test_should_be_able_to_create_file(self):
        # create a file 
        pass 

    def test_should_test_if_word_is_number(self): 
        # input("Enter the word: ") NEVER DO THIS 
        # Your test should never ask for outside input
        self.palindrome.reverse()
        self.assertEqual("a","b") 


    def test_should_be_able_to_reverse_a_string(self): 
        self.assertEqual("tac",self.palindrome.reverse())

    # tearDown is called after running EACH test
    def tearDown(self): 
        # delete the file 
        # release the resources 
        print("Fired after running each test")

unittest.main() # run the unit test 