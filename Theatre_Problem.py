#Codechef challenge problem
import numpy as np
t=int(input())
import numpy
profit=0 #total profit for the day
total_profit=0
for x in range(t):


    ma=np.zeros(shape=(4,4))
    count_movie=[1,1,1,1]
    time_movie=[1,1,1,1,]# to check whether the show is already run
    prices=[100,75,50,25]
    p_c=0
    n=int(input())
    m={'A':0,'B':1,'C':2,'D':3}
    t={'12':0,'3':1,'6':2,'9':3}
    for y in range(n):
        k = list(input().split()) # A 12
        ma[m[k[0]]][t[k[1]]]=ma[m[k[0]]][t[k[1]]]+1
    print(ma)
    z=0
    while z<4:

        print("Iteration Number %d"%z)
        indices=np.unravel_index(np.argmax(ma, axis=None), ma.shape)
        if ma[indices]==0:
            break
        print("Maximum in this iteration %f"%ma[indices])
        print(indices)
        showtime=indices[1]
        movie=indices[0]
        print("Iteration")
        if count_movie[movie]==1 and time_movie[showtime]==1:
            profit=profit+ma[indices]*prices[p_c]

            ma[movie][showtime]=0
            count_movie[movie] =0
            time_movie[showtime] = 0
            p_c=p_c+1
            print(ma)
            print("Profit=%f"%profit)
            z=z+1
        else:


            ma[movie][showtime]=0

    for i in time_movie:
        profit=profit-100*i

    total_profit=profit+total_profit
    print(profit)
    print(ma)
print(total_profit)