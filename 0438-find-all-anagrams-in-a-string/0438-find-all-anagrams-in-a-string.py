class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:

        result = []

        if len(p) > len(s):
            return result

        p_count = [0] * 26
        window_count = [0] * 26

        # Frequency of p
        for ch in p:
            p_count[ord(ch) - ord('a')] += 1

        k = len(p)

        # First window
        for i in range(k):
            window_count[ord(s[i]) - ord('a')] += 1

        # Check first window
        if window_count == p_count:
            result.append(0)

        # Sliding window
        for right in range(k, len(s)):

            # Add new character
            window_count[ord(s[right]) - ord('a')] += 1

            # Remove character leaving the window
            left = right - k
            window_count[ord(s[left]) - ord('a')] -= 1

            # Check current window
            if window_count == p_count:
                result.append(left + 1)

        return result