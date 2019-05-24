#Find angle MBC
import math
s1=int(input())
s2=int(input())

ang=math.atan(s1/s2)*(180/math.pi)
out_ang=round(ang)
degree_sign= u'\N{DEGREE SIGN}'
print("%d%s"%(out_ang,degree_sign))
