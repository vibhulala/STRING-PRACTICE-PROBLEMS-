class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n=len(s)
        for length in range(1,n):
            #string must be completely divisible 
            if n% length ==0:
                pattern=s[:length]
                repetitions=n//length
                if pattern*repetitions==s:
                    return True 
        return False 