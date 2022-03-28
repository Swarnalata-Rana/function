n=[50,40,56,23,70,12,5,10,7]
max=0
max2=0
i=0
while i<len(n):
    if n[i]>max:
        max2=max
        max=n[i]
    elif n[i]>max2:
        max2=n[i]
    i+=1
print ('first maxmum',max)
print('second maximum',max2) 