def powerValue(num,pow):
    if pow==1:
        return num

    return (num*powerValue(num,pow-1))
number=int(input('Enter any number'))
power=int(input('Enter power value'))
a=powerValue(number,power)
print(a)