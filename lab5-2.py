def abc(num):
    sum = 0
    for i in range(num):
        price = int(input("รับราคาสินค้า %d : " % (i+1)))
        sum += price
    return sum

def tax(sum):
    vat = sum*7/100
    return vat

def total(a,b):
    t = a+b
    return t


num = int(input("จำนวนสินค้า : "))
sum = abc(num)

print("ราคารวม %d : " % sum)
print("ภาษี %.2f : " % tax(sum))
print("รวมเป็นเงินทั้งหมด %.2f : " % total(sum, tax(sum)))