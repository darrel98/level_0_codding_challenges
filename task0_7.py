def celsius_to_fahrenheit(temp):
    fahrenheit = (temp * 1.8) +32
    print( "%s degree celsiuSs in fahrenheit is: %s"%(temp,fahrenheit))

celsius_to_fahrenheit(1)

def fahrenheit_to_celsius(temp):
    celsius = (temp - 32) /1.8
    print( "%s fahrenheit in celsius: %s" %(temp,round(celsius)) )

fahrenheit_to_celsius(33.8)