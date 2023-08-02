# Prime Number by normal for loop
# count=0
# for i in range(1,n):
#     if n%i==0:
#         count+=1
# if count==2:
#     print('Prime')
# else:
#     print('composite')

# prime number by recurssion 
def prime(num,i):
    if (i==1):
        return 1
    if (num%i==0):
        return 0
    return prime(num,i-1)
num=int(input('Enter any number'))
n=(prime(num,int(num/2))) 
if (n==1):
    print('Number is prime')
else:
    print('Number is composite')