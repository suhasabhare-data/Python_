# # You are given a 2D binary array arr[][] consisting of only 1s and 0s. Each row of the array is sorted in non-decreasing order. Your task is to find and return the index of the first row that contains the maximum number of 1s. If no such row exists, return -1.
# # Note:
# # 	• The array follows 0-based indexing.
# # 	• The number of rows and columns in the array are denoted by n and m respectively.
# # Examples:
# # Input: arr[][] = [[0,1,1,1], [0,0,1,1], [1,1,1,1], [0,0,0,0]]
# # Output: 2
# # Explanation: Row 2 contains the most number of 1s (4 1s). Hence, the output is 2.
# # Input: arr[][] = [[0,0], [1,1]]
# # Output: 1
# # Explanation: Row 1 contains the most number of 1s (2 1s). Hence, the output is 1.
# # Input: arr[][] = [[0,0], [0,0]]
# # Output: -1
# # Explanation: No row contains any 1s, so the output is -1.
# # Constraints:
# # 1 ≤ arr.size(), arr[i].size() ≤ 103
# # 0 ≤ arr[i][j] ≤ 1 

# # From <https://www.geeksforgeeks.org/problems/row-with-max-1s0023/1> 
# # import numpy as np
# # class Solution:
# #     def rowWithMax1s(self, arr):
# #         # code here
# #         arr = np.array(arr)
# #         row_sums = np.sum(arr, axis=1)
# #         max_index = np.argmax(row_sums)
# #         return max_index
# Find the row with maximum number of 1s

# From <https://www.geeksforgeeks.org/dsa/find-the-row-with-maximum-number-1s/> 
# Given a binary 2D array, where each row is sorted. Find the row with the maximum number of 1s. 
# Examples:  
# Input matrix : 0 1 1 1
#                         0 0 1 1
#                         1 1 1 1 
#                         0 0 0 0
# Output: 2
# Explanation: Row = 2 has maximum number of 1s, that is 4.
# Input matrix : 0 0 1 1
#                         0 1 1 1
#                         0 0 1 1  
#                         0 0 0 0
# Output: 1
# Explanation: Row = 1 has maximum number of 1s, that is 3.
# Try it on GfG Practice
# Table of Content
# • [Naive Approach] Row-wise traversal - O(M*N) Time and O(1) Space:
# • [Better Approach] Using Binary Search - O(M * logN) Time O(1) Space:
# • [Expected Approach] Traversal from top-right to outside the grid - O(M + N) Time and O(1) Space:

# [Naive Approach] Row-wise traversal - O(M*N) Time and O(1) Space:
# A simple method is to do a row-wise traversal of the matrix, count the number of 1s in each row, and compare the count with the max. Finally, return the index of the row with a maximum of 1s.
# Below is the implementation of the above approach:
# # Python implementation of the approach
# R,C = 4,4
# ​
# # Function to find the index of first index 
# # of 1 in a boolean array arr 
# def first(arr , low , high): 
# ​
#     if(high >= low): 
# ​
#         # Get the middle index 
#         mid = low + (high - low)//2 
    
#         # Check if the element at middle index is first 1 
#         if ( ( mid == 0 or arr[mid-1] == 0) and arr[mid] == 1): 
#             return mid 
    
#         # If the element is 0, recur for right side 
#         elif (arr[mid] == 0): 
#             return first(arr, (mid + 1), high); 
        
#         # If element is not first 1, recur for left side 
#         else:
#             return first(arr, low, (mid -1)); 
# ​
#     return -1 
# ​
# # Function that returns index of row 
# # with maximum number of 1s. 
# def rowWithMax1s(mat): 
# ​
#     # Initialize max values 
#     max_row_index,Max = 0,-1 
# ​
#     # Traverse for each row and count number of 1s 
#     # by finding the index of first 1 
#     for i in range(R):
# ​
#         index = first (mat[i], 0, C-1)
#         if (index != -1 and C-index > Max):
#             Max = C - index; 
#             max_row_index = i
# ​
#     return max_row_index 
# ​
# # Driver Code
# mat = [[0, 0, 0, 1], 
#       [0, 1, 1, 1], 
#       [1, 1, 1, 1], 
#       [0, 0, 0, 0]]
# print("Index of row with maximum 1s is " + str(rowWithMax1s(mat)))
# Output
# 2
# Time Complexity:  O(M*N), where M is the number of rows and N is the number of columns.
# Auxiliary Space:  O(1)
# [Better Approach] Using Binary Search - O(M * logN) Time O(1) Space:
# Since each row is sorted, we can use Binary Search to count 1s in each row. We find the index of the first occurrence of 1 in each row. The count of 1s will be equal to the total number of columns minus the index of the first 1.
# Below is the implementation of the above approach: 
# # Python3 program to find the row
# # with maximum number of 1s
# ​
# # Function to find the index
# # of first index of 1 in a
# # boolean array arr[]
# ​
# ​
# def first(arr, low, high):
#     idx = -1
#     while low <= high:
#         # Get the middle index
#         mid = low + (high - low) // 2
# ​
#         # If the element at mid is 1, then update mid as
#         # starting index of 1s and search in the left half
#         if arr[mid] == 1:
#             idx = mid
#             high = mid - 1
#         # If the element at mid is 0, then search in the
#         # right half
#         else:
#             low = mid + 1
#     return idx
# ​
# ​
# # Function that returns
# # index of row with maximum
# # number of 1s.
# def rowWithMax1s(mat):
# ​
#     # Initialize max values
#     R = len(mat)
#     C = len(mat[0])
#     max_row_index = 0
#     max = -1
# ​
#     # Traverse for each row and
#     # count number of 1s by finding
#     #  the index of first 1
#     for i in range(0, R):
#         index = first(mat[i], 0, C - 1)
#         if index != -1 and C - index > max:
#             max = C - index
#             max_row_index = i
# ​
#     return max_row_index
# ​
# ​
# # Driver Code
# mat = [[0, 0, 0, 1],
#       [0, 1, 1, 1],
#       [1, 1, 1, 1],
#       [0, 0, 0, 0]]
# print("Index of row with maximum 1s is",
#       rowWithMax1s(mat))
# Output
# 2
# Time Complexity: O(M log N) where M is the number of rows and N is the number of columns in the matrix.
# Auxiliary Space:  O(1)
# [Expected Approach] Traversal from top-right to outside the grid - O(M + N) Time and O(1) Space:
# Start from the top-right cell(row = 0, col = N - 1) and store the ans = -1. If the value in the current cell is 1, update ans with the current row and move left. Otherwise, if the current cell is 0, move to the next row:
# • If mat[row][col] == 1, update ans = row and move left by col = col - 1.
# • Else if mat[row][col] == 0, row = row + 1.
# Continue, till we move outside the grid and return ans.
# Below is the implementation of the above approach:
# # Python3 program to find the row
# # with maximum number of 1s
# ​
# # Function that returns
# # index of row with maximum
# # number of 1s.
# def rowWithMax1s(mat):
#     R = len(mat)
#     C = len(mat[0])
#     max_row = -1
#     row = 0
#     col = C - 1
# ​
#     # Move till we are inside the matrix
#     while row < R and col >= 0:
#         # If the current value is 0, move down to the next row
#         if mat[row][col] == 0:
#             row += 1
#         # Else if the current value is 1, update max_row and move to the left column
#         else:
#             max_row = row
#             col -= 1
# ​
#     return max_row
# ​
# ​
# # Driver Code
# mat = [[0, 0, 0, 1],
#       [0, 1, 1, 1],
#       [1, 1, 1, 1],
#       [0, 0, 0, 0]]
# print("Index of row with maximum 1s is",
#       rowWithMax1s(mat))
# Output
# Index of row with maximum 1s is 2
# Time Complexity: O(M+N) where M is the number of rows and N is the number of columns in the matrix.
# Auxiliary Space:  O(1)

# From <https://www.geeksforgeeks.org/dsa/find-the-row-with-maximum-number-1s/> 

