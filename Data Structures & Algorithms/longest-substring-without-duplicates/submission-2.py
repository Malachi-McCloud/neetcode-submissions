class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        left = 0
        maxLen = 0

        for right in range(len(s)):
            # shrink to remove duplicates
            while s[right] in chars:
                chars.remove(s[left])
                left += 1

            # Now we know there is nothing in it duplicate:
            chars.add(s[right])


            # Update our result
            maxLen = max(maxLen, right - left + 1)

        return maxLen
        