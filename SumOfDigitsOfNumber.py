# a=101
# b=str(a)
# sum=0
# for i in b:
#     sum+=int(i)
# print(sum)

def sum(num):
    if num<10:
        return num
    print(num)
    
    return (num%10)+sum(int(num/10))
n=int(input('Enter any Number:'))
print(sum(n))