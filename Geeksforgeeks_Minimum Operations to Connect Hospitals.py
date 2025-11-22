# Minimum Operations to Connect Hospitals
# Difficulty: MediumAccuracy: 58.24%Submissions: 11K+Points: 4
# You are given an undirected network of V hospitals numbered from 0 to V - 1, represented as a 2D array edges[][], where each element edges[i] = [u, v] denotes a direct connection between hospital u and hospital v.
# In one operation, you are allowed to remove any existing link and reconnect it between two hospitals that are currently not directly or indirectly connected.

# Your task is to determine the minimum number of operations required to make sure that all hospitals become connected, either directly or indirectly, using the given links.


# Note: If it is impossible to connect all hospitals into a single network, return -1.

# Examples:

# Input: V = 4, E = 3, edges[][] = [[0, 1], [0, 2], [1, 2]]
# Output: 1
# Explanation: Remove the connection between hospitals 1 and 2 and connect the hospitals 1 and 3.

# Input: V = 5, E = 4, edges[][] = [[0, 1], [0, 2], [2, 3], [3, 4]]
# Output: 0
# Explanation: All hospitals are already connected directly or indirectly. No rearrangement of connections is required.

# Constraints:
# 1 ≤ V ≤ 103
# 0 ≤ E ≤ V*(V-1)/2
# 0 ≤ edges[i][0], edges[i][1] < V

from collections import defaultdict

class Solution:
    def dfs(self,node,visited,graph):
        visited[node]=1
        
        for n in graph[node]:
            if not visited[n]:
                self.dfs(n,visited,graph)
    
    def minConnect(self, V, edges):
        E = len(edges)
        
        if E<V-1:
            return -1
        
        graph = defaultdict(list)
        
        for r,c in edges:
            graph[r].append(c)
            graph[c].append(r)
        
        components = 0
        
        visited = [0]*V
        
        for i in range(V):
            if not visited[i]:
                self.dfs(i,visited,graph)
                components+=1
        
        return components-1