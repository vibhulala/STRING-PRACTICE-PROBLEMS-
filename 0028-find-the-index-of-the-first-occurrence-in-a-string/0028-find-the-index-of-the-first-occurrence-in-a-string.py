class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        brute force
        n=len(haystack)
        m=len(needle)
        for i in range(n-m+1):
            j=0
            while j<m:
                if haystack[i+j]!=needle[j]:
                    break
                j+=1
            if j==m:
                return i
        return -1
        '''
        # this is one line approach to solve this by using python built-in funciton .find() "" return haystack.find(needle)""
        # here we will first create LPS array for needle 
        m=len(needle)
        lps=[0]*m
        length=0
        i=1
        while i<m:
            if needle[i]==needle[length]:
                length+=1
                lps[i]=length
                i+=1
            else:
                if length!=0:
                    length=lps[length-1]
                else:
                    lps[i]=0
                    i+=1

        #now searching needle in haystack
        n=len(haystack)
        i,j=0,0
        while i<n:
            if haystack[i]==needle[j]:
                i+=1
                j+=1
                if j==m:
                    return i-j
            else:
                if j!=0:
                    j=lps[j-1]
                else:
                    i+=1
        return -1
