
def maximum(x,y,z):
    if x > y and x > z:
        return x
    elif y >x and y > z :
        return y
    elif z >x and z >y :
        return z
    else : #execute the else part only if some numbers are equal
        return 0 

print(str(maximum(1,8,7)))