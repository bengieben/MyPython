def score(a):
    sum = int(input("คะแนนเก็บ : "))
    return sum

def jitpisai(b):
    sum = int(input("คะแนนจิตพิสัย : "))
    return sum

def midterm(c):
    sum = int(input("คะแนนกลางภาค : "))
    return sum





def beforMidterm(a, b ,c):
    sum = a + b + c
    return sum
    



print("ผลรวมคะแนนเก็บก่อนกลางภาค : %d " % beforMidterm(score(sum),jitpisai(sum),midterm(sum)))

