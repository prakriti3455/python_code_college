def unique(l1):
    l2=[]
    for num in l1:
        if num not in l2:
            l2.append(num)
    return l2
l1=[1,2,3,3,3,3,4]
print(unique(l1))








