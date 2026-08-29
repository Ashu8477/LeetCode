class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        pref=strs[0]
        for word in strs[1:]:
            while word[:len(pref)]!=pref:
                pref=pref[:-1]
                if pref=='':
                    return ''
        return pref
        