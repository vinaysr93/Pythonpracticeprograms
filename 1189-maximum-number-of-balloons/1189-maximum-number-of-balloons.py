class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        

        dic={}

        for x in text:

            if x in dic:
                dic[x]=dic[x]+1
            
            else:
                dic[x]=1
            
        word="balloon"
        word_count=0
        print(dic)
        while True:
        
            try:
                if dic['b']>=1 and dic['a']>=1 and dic['l']>=2 and dic['o']>=2 and dic['n']>=1:


                        word_count=word_count+1
                        dic['b']=dic['b']-1
                        dic['a']=dic['a']-1
                        dic['l']=dic['l']-2
                        dic['o']=dic['o']-2
                        dic['n']=dic['n']-1
                       
                    
                else:
                    break
            except:
                break
        
        return word_count

              
