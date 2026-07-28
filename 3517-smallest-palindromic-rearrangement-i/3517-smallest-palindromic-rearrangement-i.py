class Solution:
    def smallestPalindrome(self, s: str) -> str:

        hash={}
        for ch in s:
            hash[ch]=hash.get(ch,0)+1
        
        left=[]
        middle=""

        for ch in sorted(hash.keys()):
            left.append(ch*(hash[ch]//2))

            if hash[ch]%2:
                middle=ch
        
        left="".join(left)

        return left + middle + left[::-1]

        