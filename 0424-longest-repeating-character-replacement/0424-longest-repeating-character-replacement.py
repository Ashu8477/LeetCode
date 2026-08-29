class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        l=0
        max_freq=0
        maxi=0
        for i in range(len(s)):
            count[s[i]]=count.get(s[i],0)+1
            max_freq=max(max_freq,count[s[i]])

            while (i-l+1)-max_freq>k:
                count[s[l]]-=1
                l+=1
            maxi=max(maxi,i-l+1)
        return maxi
        