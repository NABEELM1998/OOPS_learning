def add7(x):
    return x+7
def isOdd(x):
    return x%2 != 0
li = [1,2,3,4,5,6]
print(filter(isOdd,li))
print(list(map(add7,list(filter(isOdd,li)))))