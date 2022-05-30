def common_letters(string1,string2):
    a = []
    for x in string1.lower() :
        if x in string2.lower():
            if x not in a:
                a.append(x)
    print("Common letters:"+ " , ".join(a))  

common_letters("THABO","LETHABO")