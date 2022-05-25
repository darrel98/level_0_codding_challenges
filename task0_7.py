def celsius_to_fahrenheit(temp):
    fahrenheit = (temp * 1.8) +32
    print( str(temp) + " degree celsiuSs in fahrenheit is: "+ str(fahrenheit))

celsius_to_fahrenheit(1)

def fahrenheit_to_celsius(temp):
    celsius = (temp - 32) /1.8
    print(str(temp) + " degree fahrenheit in celsius: " + str(round(celsius,1)) )

fahrenheit_to_celsius(33.8)