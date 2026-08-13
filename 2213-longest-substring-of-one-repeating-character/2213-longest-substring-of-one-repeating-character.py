class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:

        n = len(s)

        tree = [[None, None, 0, 0, 0, 0] for _ in range(4 * n)]

        def merge(a, b):
            leftChar = a[0]
            rightChar = b[1]

            prefix = a[2]
            suffix = b[3]

            maxLen = max(a[4], b[4])

            if a[1] == b[0]:

                maxLen = max(maxLen, a[3] + b[2])

                if a[2] == a[5]:
                    prefix = a[5] + b[2]

                if b[3] == b[5]:
                    suffix = a[3] + b[5]

            return [
                leftChar,
                rightChar,
                prefix,
                suffix,
                maxLen,
                a[5] + b[5]
            ]

        def build(node, l, r):
            if l == r:
                tree[node] = [
                    s[l],   
                    s[l],   
                    1,      
                    1,      
                    1,      
                    1       
                ]
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, l, r, idx, ch):
            if l == r:
                tree[node] = [
                    ch,
                    ch,
                    1,
                    1,
                    1,
                    1
                ]
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, ch)
            else:
                update(node * 2 + 1, mid + 1, r, idx, ch)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        build(1, 0, n - 1)

        ans = []

        for ch, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, ch)
            ans.append(tree[1][4])

        return ans