try:
    a = 10/0
except Exception as e:
    print(e)
    
a = [1,2,3,4]
try:
    print("I am in try")
    # val = a[10]
except Exception as e:
    print(e)
finally:
    print("I am in the final ")