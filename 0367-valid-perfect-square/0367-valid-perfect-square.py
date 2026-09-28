class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        '''
        this is bascically brute force appraoch here weare doing trversal from i=1 and finding the squares of each number and sequentially comparing the number with nums if found returnING TRUE  not tehn False
        i=1
        while i*i<=num:
            if i*i==num:
                return True
            i+=1
        return False
        time complexity o(root n)
        space-o(1)
        '''
        left=1 
        right=num
        while left<=right:
            mid=(left+right)//2
            if mid*mid==num:
                return True 
            elif mid*mid<num:
                left=mid+1
            else:
                right=mid-1
        return False
