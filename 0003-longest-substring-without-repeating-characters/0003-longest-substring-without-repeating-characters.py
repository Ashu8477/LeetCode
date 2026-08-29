class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ls=''
     
        maxi=0
        for ch in s:
            if ch not in ls:
                ls+=ch
                maxi=max(maxi,len(ls))
            else:
                maxi=max(maxi,len(ls))
                while ch in ls:
                    ls=ls[1:]
                ls+=ch
        return maxi


        