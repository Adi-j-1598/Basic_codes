def maxMin(a,l,max):
    if l==0:
        return max
    if l>0:
        if a[l]>max:
            max=a[l]
    return maxMin(a,l-1,max)

a=[12,234,4564,6756,83,422,456,5,56]
max=a[0]
l=len(a)-1
print(maxMin(a,l,max))
    
def maxMin(a,l,min):
    if l==0:
        return min
    if l>0:
        if a[l]<min:
            min=a[l]
    return maxMin(a,l-1,min)
a=[12,234,4564,6756,83,422,456,5,56]
min=a[0]
l=len(a)-1
print(maxMin(a,l,min))