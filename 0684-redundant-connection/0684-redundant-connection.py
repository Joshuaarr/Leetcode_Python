class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # ignore parent[0], easier for 1-indexed
        parent = [i for i in range(len(edges) + 1)] 
        rank = [1 for i in range(len(edges) + 1)]
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(x, y):
            xRoot = find(x)
            yRoot = find(y)
            # There are already connected
            if xRoot == yRoot:
                return True
            
            if rank[xRoot] < rank[yRoot]:
                parent[xRoot] = yRoot
                rank[yRoot] += rank[xRoot]
            elif rank[xRoot] >= rank[yRoot]:
                parent[yRoot] = xRoot
                rank[xRoot] += rank[yRoot]
            return False
        
        for x, y in edges:
            if union(x, y):
                return [x, y]


            

