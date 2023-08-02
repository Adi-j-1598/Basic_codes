def palindrome(num,t):
    if num<10:
        return num
    return ((num%10))+palindrome(num//10)
print(palindrome(153))