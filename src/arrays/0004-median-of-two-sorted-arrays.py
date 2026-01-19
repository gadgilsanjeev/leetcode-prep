# Problem Title: Median of Two Sorted Arrays
# LeetCode Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
# Difficulty: Hard
# Topics: Array

"""
Explanation:
    [Briefly explain your logic here in 1-2 sentences]

Complexity:
    Time: O(n) - Explain why
    Space: O(n) - Explain why
"""

from typing import List  # Import common types as needed

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num = nums1 + nums2
        num.sort()
        l = len(num)
        if l % 2 == 0:
            return float(num[l/2] + num[l/2 - 1])/2.0
        else:
            return num[(l-1)/2]