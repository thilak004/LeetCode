class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        x=n-999
        return x