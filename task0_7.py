def celsius_to_fahrenheit(temp):
    fahrenheit = (temp * 1.8) +32
    return ( f"{temp} degree celsius in fahrenheit is: {fahrenheit}")

celsius_to_fahrenheit(1)

def fahrenheit_to_celsius(temp):
    celsius = (temp - 32) /1.8
    return (f"{temp} fahrenheit in celsius: {round(celsius)}"  )

fahrenheit_to_celsius(33.8)