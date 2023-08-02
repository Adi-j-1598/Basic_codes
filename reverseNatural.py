def revNaturalNumber(num1,num2):
    if num1<num2:
        return
    print(num1,end=',')
    return revNaturalNumber(num1-1,num2)
print(revNaturalNumber(10,1))