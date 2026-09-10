class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        '''
        brute force:-isme sidha diye gaye har array ko jod ke string bana diya ek ek loop laga ke fir dono ko compare kar leneg ki equal hai ki nahi 
        str1=''
        str2=''
        for i in word1:
            str1+=i
        for j in word2:
            str2+=j
        return str1==str2
        tc -o(n)
        sc-o(n)
        '''
        '''
        str1="".join(word1)
        str2="".join(word2)
        return str1==str2
        ye yaha .join lagane se hi hamrari space complexity o(n) reh ja rhi now in optimized we wil use two pointers 
        '''
        i = j = 0
        p1 = p2 = 0

        while i < len(word1) and j < len(word2):

            # Compare current characters
            if word1[i][p1] != word2[j][p2]:
                return False

            # Move to next character
            p1 += 1
            p2 += 1

            # Current word of word1 finished
            if p1 == len(word1[i]):
                i += 1
                p1 = 0

            # Current word of word2 finished
            if p2 == len(word2[j]):
                j += 1
                p2 = 0

        # Both arrays must be completely consumed
        return i == len(word1) and j == len(word2)


