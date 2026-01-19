# Problem Title: Two Sum
# LeetCode Link: https://leetcode.com/problems/two-sum/description/
# Difficulty: Easy
# Topics: Array

"""
Explanation:
    [Briefly explain your logic here in 1-2 sentences]

Complexity:
    Time: O(n) - Explain why
    Space: O(n) - Explain why
"""

from typing import List  # Import common types as needed

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_hash = {}
        for ind in range(len(nums)):
            if nums[ind] in sum_hash:
                return [sum_hash[nums[ind]], ind]
            sum_hash[target-nums[ind]] = ind

# Local Test Cases
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Basic Example
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Test 1 Input: {nums1}, Target: {target1}")
    print(f"Test 1 Output: {sol.twoSum(nums1, target1)}") # Expected: [0, 1]
    print("-" * 20)

    # Test Case 2: Non-adjacent numbers
    nums2 = [-10, 3, 6, 2, 4]
    target2 = -6
    print(f"Test 2 Input: {nums2}, Target: {target2}")
    print(f"Test 2 Output: {sol.twoSum(nums2, target2)}") # Expected: [1, 2]