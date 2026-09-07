class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        brute force:- sabse pehle hmne ek khali group banaya jisme hm apni final separative groups enter akrenge ab strs se ek ek word uthaya aur ek falg declare kiya False ke nam se se ki abhi koi nahi mila hai similar gorup ka ab age hmne group ke variable ke nam se groups mein loop chalaya to dekha koi word hi nhi hai sala to groups.append karke ek word dala strs se utha ke ab fir next word aya to to usko sot kiya aur aur compare kiya group me dale hue word se aagr baraabar hua to usi group mein pel denege nahi hua to ek naya group banayeng jisme not found fir se action mein ayega aur kam age badhega 
        groups=[]
        for word in strs:
            found=False
            #checking every existing group
            for group in groups:
                #compare kar rhe with everyfirst word of the group 
                if sorted(word)==sorted(group[0]):
                    group.append(word)
                    found=True
                    break
            #if no matching group was found 
            if not found:
                groups.append([word])
        return groups
        ISKI TIME COMPLEXITY :-
        n = number of words
        k = average word length
        Time: O(n × k)
        SPACE:-O(N X K) FOR SORITNG the groups/outputs
        '''
        groups={}
        for word in strs:
            #sort the word to create a common key for anagrams
            key="".join(sorted(word))
            #create a new group if key does not exist 
            if key not in groups:
                groups[key]=[]
            #add the word to its corresponding group
            groups[key].append(word)
        #return all anagram groups
        return list(groups.values()) 
#'''