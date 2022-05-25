import math
side1 = 3
side2 =  4
side3 = 5
def area_of_triangle(value1,value2,value3):
    semi1 = (1/2) * (value3+ value2 + value1) #calculate the semiperemiter of triangle
    area = math.sqrt(semi1*((semi1 - value1)*(semi1-value2)*(semi1-value3)))
    print( area )

area_of_triangle(side1,side2,side3)