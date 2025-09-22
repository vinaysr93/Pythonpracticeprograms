class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        word_list=[]
        sl=len(s)
        count_words=0
        
        for x in words:
            t_copy=s
            if x in word_list:
                count_words+=1
                continue
            count=0
            for a in x:

                if a in t_copy:
                    r=t_copy.index(a)

                    if r>=0:
                        
                        t_copy=t_copy[r+1:]
                        count+=1
                    else:
                        break
                else:
                    break    

            if count==len(x):
                count_words+=1
                word_list.append(x)
        return count_words
