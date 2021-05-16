import unittest
import pytest

def palindromeChecker(str):
    return str == str[::-1]

#get user input
# userStr = input("Enter a string: ")
# ans = palindromeChecker(userStr)
 
# if (ans):
#     print("Yes")
# else:
#     print("No")

#unittest
class testCase(unittest.TestCase):
    def test_ans(self):
        #userStr = input("Enter a string: ")
        userStr = "PHP"
        ans = palindromeChecker(userStr)
        #pass
        self.assertTrue(ans)
        #fail
        self.assertFalse(ans)


if __name__ == '__main__':
    unittest.main()        

