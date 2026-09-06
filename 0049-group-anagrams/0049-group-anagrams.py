class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}

        for word in strs:
            # Count frequency of each character
            count = [0] * 26

            for ch in word:
                index = ord(ch) - ord('a')
                count[index] += 1

            # Convert list to tuple so it can be used as dictionary key
            key = tuple(count)

            # Group words having the same character frequency
            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())