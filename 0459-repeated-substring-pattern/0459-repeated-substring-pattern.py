class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        '''
        brute force :- isme hmne pehle diye hue string kki length calculate kar li use bad length to length to ek loop chalya length 1 ayi to fir n% length agr valid hua to utn hamne pattern banaay aur repeat kara ay agr repeated wala original wale str s ke barabb ho gya to bat ban gayi return tru nhai to return false

        n=len(s)
        for length in range(1,n):
            #string must be completely divisible 
            if n% length ==0:
                pattern=s[:length]
                repetitions=n//length
                if pattern*repetitions==s:
                    return True 
        return False 
        time comppexity:-o(n^2)
        space complexity:-o(n)
        '''
        '''
        better solution 
        n = len(s)

        for length in range(1, n):

            # Pattern length must divide string length
            if n % length != 0:
                continue

            valid = True

            # Compare every character with repeating pattern
            for i in range(length, n):

                if s[i] != s[i % length]:
                    valid = False
                    break

            if valid:
                return True

        return False
        '''
        #the one liner soltuion of this 
        return s in (s + s)[1:-1]
        