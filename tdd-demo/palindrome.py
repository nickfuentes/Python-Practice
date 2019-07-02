
class Palindrome: 
    def __init__(self,word): 
        self.word = word 

    def reverse(self): 
        reversed_word = ""
        for index in range(len(self.word)-1,-1,-1): 
            reversed_word += self.word[index]

        return reversed_word


