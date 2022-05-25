def vowels(string1,string2):
    a = []
    for x in string1 :
        if x in string2:
            a.append(x)
    print(*a , sep = ",")  

vowels("thabo","jacobb")