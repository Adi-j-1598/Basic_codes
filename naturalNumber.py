def naturalNumber(a,b):
    if a>b:
        return
    print(a,end=',')
    return naturalNumber(a+1,b)
print(naturalNumber(1,10))