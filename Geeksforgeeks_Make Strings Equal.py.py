# Make Strings Equal
# Difficulty: MediumAccuracy: 64.4%Submissions: 8K+Points: 4
# Given two strings s and t, consisting of lowercase English letters. You are also given, a 2D array transform[][], where each entry [x, y] means that you are allowed to transform character x into character y and an array cost[], where cost[i] is the cost of transforming transform[i][0] into transform[i][1]. You can apply any transformation any number of times on either string.

# Your task is to find the minimum total cost required to make the strings identical. If it is impossible to make the two strings identical using the available transformations, return -1.

# Examples:

# Input: s = "abcc", t = "bccc", transform[][] = [['a', 'b'], ['b', 'c'], ['c', 'a']], cost[] = [2, 1, 4]
# Output: 3
# Explanation: We can convert both strings into "bccc" with a cost of 3 using these operations:
# transform at Position 0 in s: a -> b (cost 2)
# transform at Position 1 in s: b -> c (cost 1)
# Other characters already match.
# Input: s = "az", t = "dc", transform[][] = [['a', 'b'], ['b', 'c'], ['c', 'd'], ['a', 'd'], ['z', 'c']], cost[] = [5, 3, 2, 50, 10]
# Output: 20
# Explanation: We can convert both strings into "dc" with a cost of 20 using these operations:
# transform at Position 0 in s: a -> d by path a -> b -> c -> d (cost 5 + 3 + 2 = 10)
# transform at Position 1 in s: z -> c (cost 10)
# Input: s = "xyz", t = "xzy", transform[][] = [['x', 'y'], ['x', 'z']], cost[] = [3, 3]
# Output: -1
# Explanation: It is not possible to make the two strings equal.
# Constraints:
# 1 ≤ s.size() = t.size() ≤ 105
# 1 ≤ transform.size() = cost.size() ≤ 500
# 'a' ≤ transform[i][0], transform[i][1] ≤ 'z'
# 1 ≤ cost[i] ≤ 500

class Solution:
    def minCost(self,s,t,transform,cost):
        I=10**12;D=[[I]*26 for _ in range(26)]
        for i in range(26):D[i][i]=0
        for (a,b),v in zip(transform,cost):D[ord(a)-97][ord(b)-97]=min(D[ord(a)-97][ord(b)-97],v)
        for k in range(26):
            for i in range(26):
                if D[i][k]<I:
                    for j in range(26):
                        if D[k][j]<I:D[i][j]=min(D[i][j],D[i][k]+D[k][j])
        A=0
        for x,y in zip(s,t):
            u,v=ord(x)-97,ord(y)-97
            if u!=v:
                B=min((D[u][c]+D[v][c] for c in range(26) if D[u][c]<I and D[v][c]<I),default=I)
                if B==I:return-1
                A+=B
        return A