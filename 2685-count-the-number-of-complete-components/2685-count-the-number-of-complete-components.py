class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        ans = 0

        def dfs(node):

            visited.add(node)

            nodes = 1
            edge_count = len(graph[node])

            for nei in graph[node]:

                if nei not in visited:

                    n_nodes, n_edges = dfs(nei)

                    nodes += n_nodes
                    edge_count += n_edges

            return nodes, edge_count

        for i in range(n):

            if i not in visited:

                nodes, edge_count = dfs(i)

                edge_count //= 2

                if edge_count == (nodes * (nodes - 1)) // 2:
                    ans += 1

        return ans