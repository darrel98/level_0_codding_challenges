
def area_of_triangle(value1,value2,value3):
    semi1 = (1/2) * (value3+ value2 + value1)
    area = (semi1*((semi1 - value1)*(semi1-value2)*(semi1-value3)))**(1/2)
    return area

area_of_triangle(3,4,5)