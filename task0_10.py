def common_letters(string1,string2):
    a = []
    for x in string1 :
        if x in string2:
            a.append(x)
    print("Common letters:",*a , sep = ",")  

common_letters("thabo","jacobb")