'''You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].'''

def plusOne(self, digits):
        x = ""  
        for i in digits:
            x+=str(i)
        y =  str(int(x)+1)
        return [int(i) for i in y]

digits = [1,2,3]
print(plusOne(digits))