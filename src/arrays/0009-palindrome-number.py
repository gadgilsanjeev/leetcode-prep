# Problem Title
# LeetCode Link: [Paste Link Here]
# Difficulty: [Easy/Medium/Hard]
# Topics: [Array, Hash Table, etc.]

"""
Explanation:
    [Briefly explain your logic here in 1-2 sentences]

Complexity:
    Time: O(n) - Explain why
    Space: O(n) - Explain why
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x) == str(x)[::-1]
