def sumDigit(num):
    if num==0:
        return 0
    return ((num%10 * num%10)+sumDigit(num//10))
def happy(num):
    if num==1:
        return True
    if num==4:
        return False
    return happy(sumDigit(num))
print(sumDigit(13))
print(happy(13))