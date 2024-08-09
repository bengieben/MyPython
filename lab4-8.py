def Ben(weight,height):
    bmi = weight/(height/100)**2
    return bmi
  



def a(weight,height):
    bmi = weight/(height/100)**2
    if (bmi < 18.50):
        print('น่ำหนักน้อย/ผอม')
    elif (bmi >= 18.50 and bmi <= 22.90):
        print('ปกติ(สุขภาพดี)')
    elif (bmi >= 23 and bmi <= 24.90):
        print('ท้วม/โรคอ้วนระดับ1')
    elif (bmi >= 25 and bmi <= 29.90):
        print('อ้วน/โรคอ้วนระดับ2')
    else:
        print('อ้วนมาก/โรคอ้วนระดับ3')
weight = int(input("input w : "))
height = int(input("input  h:  "))


print("เปรียบเทียบค่าbmi = %.2f " % Ben(weight,height))    
a(weight,height)
   
        
    
    
    


    

    
    