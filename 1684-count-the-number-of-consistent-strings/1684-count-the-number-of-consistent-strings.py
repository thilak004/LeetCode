class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        cnt=0
        for i in range(len(words)):
            word=list(set(words[i]))
            flag=0
            for j in range(len(word)):
                if word[j] not in allowed:
                    flag=1
                    break
            if flag==0:
                cnt+=1
        return cnt
