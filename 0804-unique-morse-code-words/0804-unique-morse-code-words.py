class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
            "....", "..", ".---", "-.-", ".-..", "--", "-.",
            "---", ".--.", "--.-", ".-.", "...", "-", "..-",
            "...-", ".--", "-..-", "-.--", "--.."
        ]
        unique=[]
        for word in words:
            code=""
            for ch in word:
                index=ord(ch)-ord('a')
                code+=morse[index]
            if code not in unique:
                unique.append(code)
        return len(unique)