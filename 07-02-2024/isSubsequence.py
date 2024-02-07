'''Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true'''

def isSubsequence(s, t):
    i = 0
    for x in t:
        if i==len(s):
            return True
        if s[i] == x:
            i+=1
    return i ==  len(s)

s = "abc"
t = "ahbgdc"
print(isSubsequence(s, t))