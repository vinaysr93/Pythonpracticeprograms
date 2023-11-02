class Solution:
    def mergeAlternately(self, word1, word2):

        l1=len(word1)
        l2=len(word2)
        
        if l1>l2:
            max_word=word1
        else:
            max_word=word2
        
        ns=[]
        for x in range(min(l1,l2)):

                a=word1[x]
                b=word2[x]
                ns.append(a)
                ns.append(b)

        if max_word:
            ns.append(max_word[min(l1,l2):])
        
        return "".join(ns)
        