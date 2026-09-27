class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        '''
        brute force 
        n=len(nums)
        for num in nums:
            c=0
            for i in nums:
                if i==num:
                    c+=1
            if c>n//2:
                return num
        '''
        '''
        better apparaoch
        n=len(nums)
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
            if freq[num]>n//2:
                return num
                here we will remove the dictionary because it is taking extra space 

        '''
        candidate=None
        c=0
        for num in nums:
            if c==0:
                candidate=num
            if num==candidate:
                c+=1
            else:
                c-=1
        return candidate