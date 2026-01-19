# Problem Title: Longest Palindromic Substring
# LeetCode Link: https://leetcode.com/problems/longest-palindromic-substring/description/
# Difficulty: Medium
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
    
    def find_max_prefix(self, current_prefix: str, other_word: str) -> str:
        for i in range(len(current_prefix)):
            if current_prefix[i] != other_word[i] or i >= len(other_word):
                return current_prefix[:i]
        return current_prefix

    def longestCommonPrefix(self, strs: List[str]) -> str:
        max_prefix = 0
        smallest_word = ""
        smallest_word_len = 200
        for i in range(len(strs)):
            if len(strs[i]) < smallest_word_len:
                smallest_word = strs[i]
                smallest_word_len = len(strs[i])
                if len(strs[i]) == 0:
                    return ""
        current_max_prefix = smallest_word
        for i in strs:
            if current_max_prefix == i:
                continue
            current_max_prefix = self.find_max_prefix(current_max_prefix, i)
        return current_max_prefix

if __name__ == "__main__":
    sol = Solution()
    strs = ["flower","flow","flight"]
    print(f"Test 1 Output: {sol.longestCommonPrefix(strs)}")
    print("-" * 20)

