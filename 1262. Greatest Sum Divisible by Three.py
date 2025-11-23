# 1262. Greatest Sum Divisible by Three
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer array nums, return the maximum possible sum of elements of the array such that it is divisible by three.

 

# Example 1:

# Input: nums = [3,6,5,1,8]
# Output: 18
# Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
# Example 2:

# Input: nums = [4]
# Output: 0
# Explanation: Since 4 is not divisible by 3, do not pick any number.
# Example 3:

# Input: nums = [1,2,3,4,4]
# Output: 12
# Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
 

# Constraints:

# 1 <= nums.length <= 4 * 104
# 1 <= nums[i] <= 104

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)
        if total % 3 == 0:
            return total
        
        # Find smallest numbers with remainder 1 and 2
        rem1, rem2 = [], []
        for num in nums:
            if num % 3 == 1:
                rem1.append(num)
            elif num % 3 == 2:
                rem2.append(num)
        
        rem1.sort()
        rem2.sort()
        
        if total % 3 == 1:
            option1 = total - (rem1[0] if rem1 else float('inf'))
            option2 = total - (rem2[0] + rem2[1] if len(rem2) >= 2 else float('inf'))
            return max(option1, option2)
        else:  # total % 3 == 2
            option1 = total - (rem2[0] if rem2 else float('inf'))
            option2 = total - (rem1[0] + rem1[1] if len(rem1) >= 2 else float('inf'))
            return max(option1, option2)