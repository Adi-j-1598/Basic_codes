def factorial(num):
    if num==1:
        return 1
    return num*factorial(num-1)
num=int(input('Enter any Number: '))
print(factorial(num))

# for i in range(1,num):
#     num=num*i
# print(num)