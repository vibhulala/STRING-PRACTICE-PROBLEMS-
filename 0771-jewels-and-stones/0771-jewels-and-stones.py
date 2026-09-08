class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        '''
        brute force approach :- isme hm kya kar rhe ki stones wale me se ek ek karke nikal rhe aur jewels me se ek ek nikal karke donon ko check akre ki barabr hai ki nahi hua to count c ko ek badha denge and break kar denege kab tk jab tk same hota rega end mein loop se bahr nikal ke return kar denege count c ko 
        c=0
        for i in stones:
            for j in jewels:
                if i==j:
                    c+=1
                    break
        return c
        '''
        set_jewels,c=set(jewels),0
        for i in stones:
            if i in set_jewels:
                c+=1
        return c
