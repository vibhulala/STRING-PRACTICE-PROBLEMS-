class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        '''
        brute force :- isme hmne simply ek ek number nikal hia diye gaye list se and usko check kiya hai aki wo even hai ya nahi jaise hi even hua hamne count +1 kiya and list khtm hote hi out of the loop returun kar diya 
        count=0
        for num in nums:
            digits=0
            while num>0:
                num//=10
                digits+=1
            if digits%2==0:
                count+=1
        return count
        time complexity-0(n)
        space comlexity-0(1)
        '''
        '''
        better approach we bascically remove the repeated division idea here we simply pic one one number from list and conver it into string and then use len() function after that we checked whtere it is even or not , if even then we increase the count +1 
        
        count=0
        for num in nums:
            if len(str(num))%2==0:
                count+=1
        return count 
        '''
        count =0
        for num in nums:
            if(10<=num<=99 or 1000<=num<=9999 or 100000<=num<=999999):
                count+=1
        return count