def countingDigits(num):
    if num<10:
        return 1
    return 1+countingDigits(num/10)
n=int(input('Enter any number'))
print(countingDigits(n))