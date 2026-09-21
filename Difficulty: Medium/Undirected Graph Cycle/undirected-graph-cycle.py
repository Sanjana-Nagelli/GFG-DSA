class Solution:
	def isCycle(self, V, edges):
	    
	    parent = [i for i in range(V)]
	    
	    rank = [0] * V

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])   
            return parent[x]

        def union(u, v):
            root_u = find(u)
            root_v = find(v)

            if root_u == root_v:
                return False

            if rank[root_u] < rank[root_v]:
                parent[root_u] = root_v
            
            elif rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
                
            else:
                parent[root_v] = root_u
                rank[root_u] += 1

            return True
            
        for u, v in edges:
            if not union(u, v):
                return True

        return False