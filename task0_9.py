def vowels(text):
    vowels =["a","e","i","o","u"]
    vowel =[]
    for x in str.lower(text) :
        if x in vowels:
            if x not in vowel:
                vowel.append(x)
    print("Vowels:" + " , ".join(vowel) )
vowels("aluwawASo")