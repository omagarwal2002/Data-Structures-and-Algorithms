'''Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000'''

def myPow(self, x: float, n: int) -> float:
        return x**n

x = 2.00000
n = 10
print(myPow(x,n))