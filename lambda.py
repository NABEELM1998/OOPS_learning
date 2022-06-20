func = lambda x,y : x+5+y
print(func(2,5))
li =[1,2,3,5]
print(list(map(lambda x:x+5,li)))
print(list(map(lambda x :x+5,(filter(lambda x : x%2 !=0,li)))))