t1=int(input())
t2=int(input())
t3=int(input())
t=0
if t1>t2 and t1>t3:
    t=(t1+t2)/2
elif t2>t3 and t2>t1:
    t=(t2+t3)/2
else:
    t=(t3+t1)/2
print(t)







