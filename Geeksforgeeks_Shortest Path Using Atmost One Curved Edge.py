# Given an undirected, connected graph with V vertices numbered from 0 to V-1 and E double-edges, represented as a 2D array edges[][]. Each double-edge is represented by a tuple (x, y, w1, w2), which indicates that there are two edges between vertices x and y: a straight edge with weight w1 and a curved edge with weight w2.

# You are given two vertices a and b and you have to go from a to b through a series of edges such that in the entire path, you can use at most 1 curved edge. Your task is to find the shortest path from a to b satisfying the above condition.
# If no such path exists that satisfies this restriction, return -1.

# Note: It is guaranteed that the shortest path value will fit in a 32-bit integer.

# Examples:

# Input: V = 4, E = 4, a = 1, b = 3, edges[][] = [[0, 1, 1, 4], [0, 2, 2, 4], [0, 3, 3, 1], [1, 3, 6, 5]]

# Output: 2
# Explanation:
# We can follow the path 1 -> 0 -> 3, this gives a distance of 1+3 = 4 if we follow all straight paths. But we can take the curved path  from 0 -> 3, which costs 1. This will result in a cost of 1 + 1 = 2.
# Input: V = 2, E = 1, a = 0, b = 1, edges[][] = [[0, 1, 4, 1]]

# Output: 1
# Explanation:
# Take the curved path from 0 to 1 which costs 1. 

# Constraints:
# 1 ≤ V ≤ 106
# 0 ≤ E ≤ 106
# 0 ≤ a, b ≤ V - 1
# 0 ≤ edges[i][0], edges[i][1] ≤ V-1
# 0 ≤ edges[i][2], edges[i][3] ≤ 104

class Solution:
    def shortestPath(self, V, a, b, edges):
        INF = 10**9
        
        # Build adjacency list: each edge has straight weight w1 and curved weight w2
        adj = [[] for _ in range(V)]
        for u, v, w1, w2 in edges:
            adj[u].append((v, w1, w2))
            adj[v].append((u, w1, w2))  # undirected graph assumption
        
        # dist[node][usedCurveFlag]
        dist = [[INF, INF] for _ in range(V)]
        
        # PQ stores state in the form of (distance, node, usedCurve)
        pq = []
        
        # Start from 'a' without using any curved edge
        dist[a][0] = 0
        heapq.heappush(pq, (0, a, 0))
        
        while pq:
            d, node, used = heapq.heappop(pq)
            
            if d != dist[node][used]:
                continue
            
            # Explore all neighbors of 'node'
            for nxt, w1, w2 in adj[node]:
                
                # Take straight edge - usedCurve remains same
                if dist[nxt][used] > d + w1:
                    dist[nxt][used] = d + w1
                    heapq.heappush(pq, (dist[nxt][used], nxt, used))
                
                # Use curved edge (only if not used before)
                if used == 0:
                    if dist[nxt][1] > d + w2:
                        dist[nxt][1] = d + w2
                        heapq.heappush(pq, (dist[nxt][1], nxt, 1))
        
        # Minimum of both possibilities (curved edge used or not)
        ans = min(dist[b][0], dist[b][1])
        
        return -1 if ans >= INF else ans
