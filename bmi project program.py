print "Welcome to our organization please give details of employees\nIf your details are completed or quit from program then prees 1in block of name for final result else type any no"

try:
    res=[]
    i=0
    while i<=5:
        q=int(raw_input("enter input"))
        if q==1:
            break
        else:
            n=raw_input("enter name of emp:")
            a=int(raw_input("enter age of emp:"))
            w=float(raw_input("enter weight of emp:"))
            h=float(raw_input("enter height of emp in meters:"))
            BMI= (w)/(h)**2
            i=i+1
            print "BMI=",BMI
            res.append(BMI)
    for i in res:
        pass
    value=sum(res)
    value1=value/len(res)
    if value1<=20:
        print "your orgnization health is not good"
    else:
        print"your organization health is good"
except ValueError as err:
    print "we are expecting only digits"
except ZeroDivisionError as err:
    print"you don't give any employee detail "
finally:
    print "Thank You"
    
     
    
            
            
            