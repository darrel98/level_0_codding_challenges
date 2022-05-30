def to_hours_and_minutes(value):
    if value // 60 > 0 :
        hours = value // 60
        if value % 60 > 0 :
            minutes = value % 60
            if hours > 1 and minutes > 1:
                 print(f"{hours} hours , {minutes} minutes" )
        
            elif hours > 1 and minutes == 1:
               print(f"{hours} hours , {minutes} minute" )
            elif hours ==1 and minutes == 1:
                print(f"{hours} hour , {minutes} minute" )
            elif hours ==1 and minutes > 1:
                print(f"{hours} hour , {minutes} minutes")
        elif hours ==1 :
            print(f"{hours} hour , {0} minutes")   
        else :
            print(f"{hours} hours , {0} minutes" )
    elif value > 1 :
           print(f"{value} minutes")
    elif value ==0:
         print(f"{value} hours , {value} minutes" )
    else :
        print( f"0 hours , {value} minute" )
        


to_hours_and_minutes(80)