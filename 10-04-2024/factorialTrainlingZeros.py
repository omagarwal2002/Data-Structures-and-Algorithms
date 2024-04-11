'''Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero'''

def trailingZeroes(self, n: int) -> int:
        count=0
        while n>0:
           n//=5
           count+=n
        return count

n = 3
print(trailingZeroes(n))