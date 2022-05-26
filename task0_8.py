def to_hours_and_minutes(value):
    if value // 60 > 0 :
        hours = value // 60
        if value % 60 > 0 :
            minutes = value % 60
            if hours > 1 and minutes > 1:
                print(str(hours) + "hours" + str(minutes) + "minutes" )
        
            elif hours > 1 and minutes == 1:
                print(str(hours) + "hours," + str(minutes) + "minute" )
            elif hours ==1 and minutes == 1:
                print(str(hours) + "hour," + str(minutes) + "minute" )
            elif hours ==1 and minutes > 1:
                print(str(hours) + "hour," + str(minutes) + "minutes" )
        elif hours ==1 :
            print(str(hours) + "hour" + str(0) + "minutes" )   
        else :
            print(str(hours) + "hours" + str(0) + "minutes" )
    elif value > 1 :
           print( str(value) + "minutes" )
    elif value ==0:
         print(str(value) + "hours" + str(value) + "minutes" )
    else :
        print( "0hours ," + str(value) + "minute" )
        


to_hours_and_minutes(1)