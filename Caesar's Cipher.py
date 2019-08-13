

# Caesar's Cipher

n=int(input())
s=input()
k=int(input())
c_s=[]
for x in range(n):
    if s[x].isalpha():

        t=ord(s[x])#Prints the ascii value here

        nt=t+k

        if t>96 and t<123:

            while((nt<97 or nt>122)):
                nt=(nt-122)+96

        elif (t>64 and t<91):
            while((nt<65 or nt>90)):
                nt=(nt-90)+64


        nt=chr(nt)


    else:
        nt=s[x]

    c_s.append(nt)

ns="".join(c_s)
print(ns)