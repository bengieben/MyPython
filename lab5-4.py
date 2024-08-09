def F(c):
    degree = (9/5)*c+32
    return degree

def K(c):
    degree = c+273.15
    return degree

c = int(input("องศาเซลเซียส : "))

print("อุณหภูมิ F ที่แปลงได้ : %.2f " % F(c))
print("อุณหภูมิ K ที่แปลงได้ : %.2f " % K(c))
    