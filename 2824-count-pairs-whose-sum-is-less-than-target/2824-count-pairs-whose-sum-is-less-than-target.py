class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        c=0
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if nums[i]+nums[j]<target and i<j:
                    c+=1
        return c
