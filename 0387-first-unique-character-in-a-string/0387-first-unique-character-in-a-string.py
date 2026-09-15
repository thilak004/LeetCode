class Solution:
    def firstUniqChar(self, s: str) -> int:
        s1=list(s)
        for i in range(len(s)):
            ch=s1[i]
            if s.count(ch)==1:
                return i
        return -1
        