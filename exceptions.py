try:                    
    t =2
    if t == 2:
        raise Exception
except FileNotFoundError as e:
    print("Sorry no such file")
except Exception as e:
    print("sorry something went wrong")
else:
    print("hello baby")
finally:
    print("jndf")


