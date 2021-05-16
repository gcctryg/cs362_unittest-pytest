import unittest

def countWords(str):
    return len(str.split())



class testCase(unittest.TestCase):
    def test_ans(self):
        #userStr = input("Enter a sentence: ")
        userStr = "This is an activity"
        ans = countWords(userStr)
        #pass
        self.assertEqual(ans, 3)
        #fail
        self.assertEqual(ans, 4)

if __name__ == '__main__':
    unittest.main()   

#print("The number of words are: " + str(ans))


