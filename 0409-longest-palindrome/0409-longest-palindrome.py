class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq={}
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        length=0
        has_odd=False
        for count in freq.values():
            length+=(count//2)*2
            if count%2==1:
                has_odd=True
        if has_odd:
            length+=1
        return length
        