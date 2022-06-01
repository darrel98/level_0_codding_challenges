
def area_of_triangle(value1,value2,value3):
    semiperimeter = (1/2) * (value3+ value2 + value1)
    area = (semiperimeter*((semiperimeter - value1)*(semiperimeter-value2)*(semiperimeter-value3)))**(1/2)
    return area

area_of_triangle(3,4,5)