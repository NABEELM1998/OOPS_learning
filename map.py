li = [1,2,3,4,5,6,7,8,9]
def func(c):
    return c*c
    #map takes every element of the iterable and applies the function to each of them.
print(list(map(func,li))) 
print([func(x) for x in li])