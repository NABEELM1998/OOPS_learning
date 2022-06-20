""" LEGB
Local , Enclosing , Global, Built in
python will first check the vaiable in local then enclosing then it will check on the 
global and then atlast it will check on the bultin scope

 """




""" 
x = "global_x"  
def scope():
    global x
    x = "local_x"
    print(x)

scope()
print(x)
 """
z = "global_z"
def outer():
    z = "outer_z"
    def inner():
        global z
        z= "non local"
        print(z)
    inner()
    print(z)
outer()
print(z)