class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # Create search table for pairs(graph)
        graph = defaultdict(list)
        for x, y in adjacentPairs:
            graph[x].append(y)
            graph[y].append(x)
        
        # Find one end of the graph
        for num in graph:
            if len(graph[num]) == 1:
                start = num
                break
        
        res = []
        # depth first search
        def dfs(node, prev):
            res.append(node)

            for num in graph[node]:
                if num != prev:
                    dfs(num, node)

        dfs(start, None)
        return res