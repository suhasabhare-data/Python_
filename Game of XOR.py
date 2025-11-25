# Game of XOR
# Difficulty: MediumAccuracy: 50.77%Submissions: 44K+Points: 4
# You are given an integer array arr[]. The value of a subarray is defined as the bitwise XOR of all elements in that subarray.
# Your task is to compute the bitwise XOR of the values of all possible subarrays of arr[].

# Examples:

# Input: arr[] = [1, 2, 3] 
# Output: 2
# Explanation:
# xor[1] = 1
# xor[1, 2] = 3
# xor[2, 3] = 1
# xor[1, 2, 3] = 0
# xor[2] = 2
# xor[3] = 3
# Result : 1 ^ 3 ^ 1 ^ 0 ^ 2 ^ 3 = 2
# Input: arr[] = [1, 2]
# Output: 0
# Explanation:
# xor[1] = 1
# xor[1, 2] = 3
# xor[2] = 2
# Result : 1 ^ 3 ^ 2 = 0
# Constraints:
# 1 ≤ arr.size() ≤ 105
# 0 ≤ arr[i] ≤ 109


class Solution:
    def subarrayXor(self, arr):
        # code here 
        result = 0
        n = len(arr)
        for i in range(n):
            if (i + 1) % 2 != 0 and (n - i) % 2 != 0:
            # Include element in final XOR
                result ^= arr[i]
        return result