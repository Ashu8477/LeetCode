class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ls=set()
        l=0
        maxi=0
        for ch in s:
            while ch in ls:
                ls.remove(s[l])
                l+=1
            ls.add(ch)
            maxi=max(maxi,len(ls))
        return maxi


        