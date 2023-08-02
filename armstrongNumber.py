def armStrong(num):
    if num<10:
        return num
    return ((num%10)**3)+armStrong(int(num/10))
a=int(input('Enter any Number:'))
b=armStrong(a)
if b==a:
    print('number is armstrong')
else:
    print('number is not an armstrong')