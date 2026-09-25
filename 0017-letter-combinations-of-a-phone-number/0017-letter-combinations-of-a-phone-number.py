class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        ans=[]
        def solve(path,idx):
            if idx==len(digits):
                ans.append(path)
                return 

            letters=phone[digits[idx]]

            for ch in letters:
                path+=ch

                solve(path,idx+1)

                path=path[:-1]
        solve('',0)
        return ans


            

                
