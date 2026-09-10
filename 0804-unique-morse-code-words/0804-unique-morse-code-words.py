class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        '''
        bruet froce:- isme pehle morse code ka main list bana diya fir ek fianl result sto ke liye unique[] bbana then har word ko character by charcter traverse akrke mrse me badla agr unique nahi rha to append akr denege unique maien and retunr kar deneg uniwue ki length isme thoda duplicates ko do bar traverse akrn apad rha 
        tc-o(n^2+nxk)
        sc-o(nxk)
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
        '''
        morse = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
            "....", "..", ".---", "-.-", ".-..", "--", "-.",
            "---", ".--.", "--.-", ".-.", "...", "-", "..-",
            "...-", ".--", "-..-", "-.--", "--.."
        ]
        unique=set()
        for word in words:
            code=[]
            for ch in word:
                index=ord(ch)-ord('a')
                code.append(morse[index])
            unique.add("".join(code))
        return len(unique)