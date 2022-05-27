def to_hours_and_minutes(value):
    if value // 60 > 0 :
        hours = value // 60
        if value % 60 > 0 :
            minutes = value % 60
            if hours > 1 and minutes > 1:
                 print("%shours, %sminutes" %(hours,minutes))
        
            elif hours > 1 and minutes == 1:
               print("%shours, %sminute" %(hours,minutes))
            elif hours ==1 and minutes == 1:
                print("%shour, %sminute" %(hours,minutes))
            elif hours ==1 and minutes > 1:
                print("%shour, %sminutes"%(hours,minutes))
        elif hours ==1 :
            print("%shour, %sminutes"%(hours,0) )   
        else :
            print("%shours, %s minutes"%(hours,0) )
    elif value > 1 :
           print("%sminutes" %(value))
    elif value ==0:
         print("%s hours, %sminutes"%(value,value) )
    else :
        print( "0hours, %s minute" %(value))
        


to_hours_and_minutes(70)