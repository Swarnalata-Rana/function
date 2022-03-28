def fun(list):
    i=0
    pos=0
    neg=0
    while i<len(list):
        if list[i]>=0:
            pos=pos+1
        elif list[i]<=0:
            neg=neg+1
        i=i+1
    print("positive no",pos)
    print("negative no",neg)
fun(list([2,-7,5,-64,-14]))