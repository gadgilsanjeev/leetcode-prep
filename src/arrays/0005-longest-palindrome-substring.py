class Solution:
    def _is_palindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i < j:
            if not s[i] == s[j]:
                return False
            i += 1
            j -= 1
        return True

    def _find_palindrome_substring_for_given_length(self, s: str, i: int) -> str:
        for k in range(0, len(s)-i+1):
            for j in range(k, len(s)-i+1, i):
                if self._is_palindrome(s[j:j+i]):
                    return s[j:j+i]
        return None
    
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s), 0, -1):
            palindrome_substring = self._find_palindrome_substring_for_given_length(s, i)
            if palindrome_substring:
                return palindrome_substring
    
if __name__ == "__main__":
    sol = Solution()
    s = "xaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaa"
    print(f"Test 1 Input: {s}")
    print(f"Test 1 Output: {sol.longestPalindrome(s)}")
    print("-" * 20)