#ชนิดข้อมูล Dictionary
x = {
    'name' : "เบนจามิน" ,
    "age":17,
    "wt":66,
    "h":173
    }
print(x)
print("สวัสดีครับคุณ %s " % x["name"])
print("พ.ศ.เกิด %d อายุ %d" % (2567-x["age"], x["age"]))
print("น้ำหนัก %d ส่วนสูง %d " % (x["wt"], x["h"]))