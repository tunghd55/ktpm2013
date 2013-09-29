#test.py
#Name: Hoang Duc Tung
#ID  : 10020413

import unittest
import triangle
import math

class test(unittest.TestCase):
    
    #Kiem tra tam giac deu
    def testTamGiacDeu1(self):
        self.assertEqual(triangle.detect_triangle(10, 10, 10),\
            "Tam giac deu!")
    def testTamGiacDeu2(self):
        self.assertEqual(triangle.detect_triangle(1, 1, 1),\
            "Tam giac deu!")
    def testTamGiacDeu3(self):
        self.assertEqual(triangle.detect_triangle(2**32-1, 2**32-1, 2**32-1),\
            "Tam giac deu!")
    def testTamGiacDeu4(self):
        self.assertEqual(triangle.detect_triangle(1e-30, 1e-30, 1e-30),\
            "Tam giac deu!")

    #Kiem tra tam giac vuong can
    def testTamGiacVuongCan1(self):
        self.assertEqual(triangle.detect_triangle(1, 1, math.sqrt(2)),\
            "Tam giac vuong can!")
    def testTamGiacVuongCan2(self):
        self.assertEqual(triangle.detect_triangle(1, math.sqrt(2), 1),\
            "Tam giac vuong can!")
    def testTamGiacVuongCan3(self):
        self.assertEqual(triangle.detect_triangle(math.sqrt(2), 1, 1),\
            "Tam giac vuong can!")
    def testTamGiacVuongCan4(self):
        self.assertEqual(triangle.detect_triangle(math.sqrt(2), 1, 1),\
            "Tam giac vuong can!")


    #Kiem tra tam giac can
    def testTamGiacCan1(self):
        self.assertEqual(triangle.detect_triangle(3, 3, 4),\
            "Tam giac can!")
    def testTamGiacCan2(self):
        self.assertEqual(triangle.detect_triangle(2**32-1, 2**32-1, 1),\
            "Tam giac can!")
    def testTamGiacCan3(self):
        self.assertEqual(triangle.detect_triangle(2**32-1, 1, 2**32-1),\
            "Tam giac can!")
    def testTamGiacCan4(self):
        self.assertEqual(triangle.detect_triangle(1, 2**32-1, 2**32-1),\
            "Tam giac can!")

    #Kiem tra tam giac vuong
    def testTamGiacVuong1(self):
        self.assertEqual(triangle.detect_triangle(3, 4, 5),\
            "Tam giac vuong!")
    def testTamGiacVuong2(self):
        self.assertEqual(triangle.detect_triangle(4e-30, 3e-30, 5e-30),\
            "Tam giac vuong!")
    def testTamGiacVuong3(self):
        self.assertEqual(triangle.detect_triangle(5*2**29, 4*2**29, 3*2**29),\
            "Tam giac vuong!")

    #Kiem tra tam giac thuong
    def testTamGiacThuong1(self):
        self.assertEqual(triangle.detect_triangle(6e-4, 4e-4, 7e-4),\
            "Tam giac thuong!")
    def testTamGiacThuong2(self):
        self.assertEqual(triangle.detect_triangle(4, 6, 7),\
            "Tam giac thuong!")
    def testTamGiacThuong3(self):
        self.assertEqual(triangle.detect_triangle(2**32-1, 2**32-2, 3),\
            "Tam giac thuong!")

    #Kiem tra khong phai tam giac
    def testKhongLaTamGiac1(self):
        self.assertEqual(triangle.detect_triangle(1, 2, 6),\
            "Khong phai tam giac!")
    def testKhongLaTamGiac2(self):
        self.assertEqual(triangle.detect_triangle(1e-4, 2e-4, 6e-4),\
            "Khong phai tam giac!")
    def testKhongLaTamGiac3(self):
        self.assertEqual(triangle.detect_triangle(2**32-1, 1, 2),\
            "Khong phai tam giac!")
    def testKhongLaTamGiac4(self):
        self.assertEqual(triangle.detect_triangle(1, 1e-30, 2**32-1),\
            "Khong phai tam giac!")

    
    #Kiem tra ngoai khoang gia tri
    def testNgoaiKhoangGiaTri1(self):
        self.assertEqual(triangle.detect_triangle(-1, 4, 5),\
            "Ngoai khoang gia tri!")
    def testNgoaiKhoangGiaTri2(self):
        self.assertEqual(triangle.detect_triangle(2, 4, 2**33),\
            "Ngoai khoang gia tri!")
    def testNgoaiKhoangGiaTri3(self):
        self.assertEqual(triangle.detect_triangle(-1, 4, 2**32),\
            "Ngoai khoang gia tri!")
    def testNgoaiKhoangGiaTri4(self):
        self.assertEqual(triangle.detect_triangle(-1, 2**32, -1),\
            "Ngoai khoang gia tri!")
    

    #Kiem tra khong phai kieu gia tri
    def testKhongDungKieu1(self):
        self.assertEqual(triangle.detect_triangle('a', 'b', 'c'),\
            "Khong dung kieu!")
    def testKhongDungKieu2(self):
        self.assertEqual(triangle.detect_triangle('a', 1, 'c'),\
            "Khong dung kieu!")
    def testKhongDungKieu2(self):
        self.assertEqual(triangle.detect_triangle(1, 1, 'c'),\
            "Khong dung kieu!")
    def testKhongDungKieu2(self):
        self.assertEqual(triangle.detect_triangle(1, 'b', 'c'),\
            "Khong dung kieu!")
    def testKhongDungKieu1(self):
        self.assertEqual(triangle.detect_triangle(1, 'b', -2),\
            "Khong dung kieu!")
    

def main():
    unittest.main()

if __name__ == "__main__":
    main()
