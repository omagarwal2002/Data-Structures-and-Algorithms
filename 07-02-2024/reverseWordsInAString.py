'''Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"'''

def reverseWords(s):
        s= s.strip()
        x = s.split(" ")[::-1]
        g = []
        for i in x:
            if len(i)>=1:
                g.append(i)
        t = g[0]
        for i in range(1,len(g)):
            t+=" "
            t+= g[i]
        return t
        
s = "the sky is blue"
print(reverseWords(s))