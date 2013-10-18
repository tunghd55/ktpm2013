import input
import unittest
import inspect
import itertools

arr = []
array =[]
doc = input.main.__doc__

    
#------------So bien--------------------------------------- 
num = doc.count(':') # Dem so bien bang so ki tu ':'
print "Number of var : \n %i " %num


#----------Doc gia tri cua bien----------------------------
i = 0
j = -1   
while(i<len(doc)):
    tmp = ''
    if(doc[i]=='['):
        k = i+1
        while(doc[k]!=';'):
            tmp += doc[k]
            k+=1
        a = int(tmp)
        tmp = ''
        k+=1
        while(doc[k]!=']'):
            tmp += doc[k]
            k+=1
        b = int(tmp)
        array[j].append(a)
        array[j].append(b)
        arr[j].append((a+b)/2)
        tmp = ''
            
    if((i+1)<len(doc) and doc[i+1]==':'):
        j+=1
        arr.append([])
        array.append([])
        
    i+=1
print "\nArray of value : "
print array


#-------------Exception----------


for i in range (0, len(array) ):
        for j in range(0, len(array[i])-2,2):
            if (array[i][j+2]-array[i][j+1])*(array[i][j+3]-array[i][j]) < 0:
                raise Exception("wrong input")
            if len(array[i]) > 4 and ( array[i][4]-array[i][1])*(array[i][5]-array[i][0]) < 0 :
                raise Exception("wrong input")
                      
#-------------Test--------------
            
print "\nArray of test case : "
print arr          

class TestSequense(unittest.TestCase):
    pass

def test_generator(a, b):
    def test(self):
        self.assertEqual(a,b)
    return test

if __name__ == '__main__':
    print "\nTest CASE : "
    for element in itertools.product(*arr):
        print element
        test_name = 'test_%s' %str(element)
        test = test_generator(input.main(*element) , "abcdxyz")
        setattr(TestSequense, test_name, test)
    unittest.main()
