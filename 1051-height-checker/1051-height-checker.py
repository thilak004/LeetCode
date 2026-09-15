class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        r=[]
        r=sorted(heights)
        c=0
        for i in range(len(heights)):
            if heights[i]!=r[i]:
                c+=1
        return c
