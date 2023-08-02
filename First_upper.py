def first_upper(str,i):
    l=len(str)
    if i>=l:
        return 
    if str[i].isupper():
        return str[i]
    return first_upper(str,i+1)
str=input('Enter any string: ')
print(first_upper(str,0))
    