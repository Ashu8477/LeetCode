class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        matcher: dict[str, list[str]] = {}
        for s in strs:
            s_sorted = tuple(sorted(s))
            if s_sorted in matcher:
                matcher[s_sorted].append(s)
            else:
                matcher[s_sorted] = [s]
        return list(matcher.values())