class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:

        def parse(s, i):
            res = set()
            current = {""}

            while i < len(s) and s[i] != '}':
                
                if s[i] == ',':
                    res |= current
                    current = {""}
                    i += 1

                elif s[i] == '{':
                    group, i = parse(s, i + 1)

                    # Cartesian product
                    current = {
                        a + b
                        for a in current
                        for b in group
                    }

                else:
                    # Normal character
                    current = {
                        word + s[i]
                        for word in current
                    }
                    i += 1

            res |= current

            # Skip '}'
            if i < len(s) and s[i] == '}':
                i += 1

            return res, i

        result, _ = parse(expression, 0)

        return sorted(result)