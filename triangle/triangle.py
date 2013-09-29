#triangle.py
#Name : Hoang Duc Tung
#ID   : 10020413

import math
def detect_triangle(a, b, c):
    e = 10**-9

    if (type(a) in [int, float, long] and type(b) in [int, float, long] and type(c) in [int, float, long]):
        if (a>0 and b>0 and c>0) and (a<2**32 and b<2**32 and c<2**32):
            if (a+b>c and b+c>a and a+c>b):
                if (a==b==c):
                    return "Tam giac deu!"
                elif (a==b or a==c or b==c):
                    if (math.fabs(a**2+b**2-c**2)<e\
                    or math.fabs(a**2+c**2-b**2<e)\
                    or math.fabs(b**2+c**2-a**2<e)):
                        return "Tam giac vuong can!"
                    else:
                        return "Tam giac can!"
                elif (math.fabs(a**2+b**2-c**2)<e or math.fabs(a**2+c**2-b**2)<e or math.fabs(b**2+c**2-a**2)<e):
                    return "Tam giac vuong!"
                else:
                    return "Tam giac thuong!"
            else:
                return "Khong phai tam giac!"
        else:
            return "Ngoai khoang gia tri!"
    else:
        return "Khong dung kieu!"