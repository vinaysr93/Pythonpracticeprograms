class Solution:
    def findComplement(self, num):

        s=str(format(num,'b'))
        print(s)
        ns=[]
        for x in s:

            if x=='0':
                ns.append(1)
            else:
                ns.append(0)

        print(ns)
        i=0
        for y in range(len(ns)):

           i=i+(pow(2,y)*ns[len(ns)-y-1])

        return(i)


