class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        char=set()
        ans=0
        i=0

        for j in range(len(s)):

            while s[j] in char:
                char.remove(s[i])
                i+=1
            char.add(s[j])
            ans=max(ans,j-i+1)
        return ans


        