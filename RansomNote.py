class Solution:
    def canConstruct(self, ransomNote, magazine):

        lrn=len(ransomNote)
        lmg=len(magazine)
        rN={}
        mG={}
        for x in range(len(ransomNote)):


            if ransomNote[x] in rN:
                rN[ransomNote[x]]=rN[ransomNote[x]]+1
            else:
                rN.setdefault(ransomNote[x],1)

        for y in range(len(magazine)):

            if magazine[y] in mG:
                mG[magazine[y]] = mG[magazine[y]] + 1
            else:
                mG.setdefault(magazine[y], 1)
        count=0
        for i in rN:

            if i in mG:

                a=rN[i]
                b=mG[i]
                if a<=b:
                    count=count+1
                else:
                    count=-1
                    break


            else:
                count=-1

                break

        print(rN)
        print(mG)

        if (lrn == 0 and lmg == 0) or (lrn==0 and lmg>0):
            print(True)

        elif count>0:
            print(True)

        else :
            print (False)


q=Solution()
q.canConstruct("fihjjjjei","hjibagacbhadfaefdjaeaebgi")