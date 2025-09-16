class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int):

        al1=[]
        ab1=[]
        bl1=[]
        bb1=[]
       

        for h in range(ax1,ax2+1):
            al1.append(h)

        for i in range(bx1,bx2+1):
            bl1.append(i)

        for j in range(ay1,ay2+1):
            ab1.append(j)

        for k in range(by1,by2+1):
            bb1.append(k)   

        print(al1)
        print(ab1)
        print(bl1)
        print(bb1)

        a1=(max(al1)-min(al1))*(max(ab1)-min(ab1))
        a2=(max(bl1)-min(bl1))*(max(bb1)-min(bb1))
        print ("area",a1,a2)

        l_intersect= set(al1).intersection(set(bl1))
        b_intersect= set (ab1).intersection(set(bb1))
       
        print("Intersect Area",l_intersect,b_intersect)
        if not l_intersect:
            l_intersect=[0]
        
        if not b_intersect:
            b_intersect=[0]
        
        print(l_intersect)
        print(b_intersect)
        b1=abs((max(l_intersect)-min(l_intersect))*(max(b_intersect)-min(b_intersect)))

        return (a1+a2-b1)