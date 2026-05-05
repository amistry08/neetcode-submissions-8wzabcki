class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        time = {node: float("inf") for node in range(1, n + 1)}
        adj = {i:[] for i in range(1, n+1)}
        for u, v, t in times:
            adj[u].append((v, t))

        def dfs(node, tim):
            if tim >= time[node]:
                return

            time[node] = tim
            for i, j in adj[node]:
                dfs(i, tim + j)
        

        dfs(k,0)
        res = max(time.values())
        return res if res < float('inf') else -1
