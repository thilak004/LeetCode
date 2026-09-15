class Solution:
    def countRotations(self, s: str, k: int) -> int:
        n=len(s)
        ans=0
        for i in range(n):
            rot=s[i:]+s[:i]
            score=sum(1 for j in range(n-1) if rot[j]==rot[j+1])
            if score==k:
                ans+=1
        return ans
        