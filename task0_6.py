
def maximum(number1,number2,number3):
    if number1 > number2 and number1 > number3:
        return number1
    elif number2 >number1 and number2 > number3 :
        return number2
    elif number3 >number1 and number3 >number2 :
        return number3
    elif number1 == number2:
        return number1
    elif number1 == number3:
        return number1
    elif number3 == number2 :
        return number3
    else :
        return 0 

print(str(maximum(1,8,9)))