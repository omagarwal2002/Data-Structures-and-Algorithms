'''Given an integer x, return true if x is a 
palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.'''

def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

x = 121
print(isPalindrome(x))