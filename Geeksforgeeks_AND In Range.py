
# You are given two integers l and r. Find the result after applying the series of Bitwise AND ( & ) operation on every natural number between the range l to r (including both).

# Examples:

# Input: l = 8, r = 13
# Output: 8
# Explanation: 
# 8 AND 9 AND 10 AND 11 AND 12 AND 13 = 8.
# Input: l = 2, r = 3
# Output: 2
# Explanation: 2 AND 3 = 2.
# Constraints:
# 1 ≤ l ≤ r ≤ 109

class Solution:
    def andInRange(self, l, r):
        shift = 0
        while l < r:
            l >>= 1
            r >>= 1
            shift += 1
        return l << shift

