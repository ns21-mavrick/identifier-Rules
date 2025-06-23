# DEVELOP 20 valid use_cases using 5 rules of an identifier
print("===Rule-1===")  #only allows characters from AtoZ, atoz & numbering from 0to9
print()
#Example-1
print("Example-1")
import time
ABC=678
print("The value of ABC is:",ABC)
print()
print("The address is:",id(ABC))
print()
print("The data type is:",type(ABC))
print()
time.sleep(3)
print("End of an application")
print() 

#Example-2
print("Example-2")
import time
abc=666
print("The Value of abc is ",abc)
print()
print("The address is",id(abc))
print()
print("the data type is:",type(abc))
print()
time.sleep(3)
print("End of an application")
print()

#Example-3
print("Example-3")
import time
ABC123=5000
print("The value of ABC123 is:",ABC123)
print()
print("The address is:",id(ABC123))
print()
print("data type is",type(ABC123))
time.sleep(3)
print()
print("The End of an appication")
print()

#Example-4
print("Example-4")
import time
abc123=5000
print("The value of abc123 is:",abc123)
print()
print("The address is:",id(abc123))
print()
print("data type is",type(abc123))
time.sleep(3)
print()
print("The End of an appication")
print()

#Example-5
print("Example-5")
import time
_=567
print("Value of _ is:",_)
print()
print("the address is:",id(_))
print()
print("data type is",type(_))
time.sleep(3)
print()
print("The End of an application")

#Example-6
print("Example-6")
import time
ABC_abc_123=567
print("Value of ABC_abc_123 is:",ABC_abc_123)
print()
print("the address is:",id(ABC_abc_123))
print()
print("data type is",type(ABC_abc_123))
time.sleep(3)
print()
print("The End of an application")
print()


#Rule-2 A variable should not start with a number
print("===Rule-2===")
print()
print("Example-1")
import time
A12345=9999
print("The value is:",A12345)
print()
print("Address is:",id(A12345))
print()
print("datatype is",type(A12345))
print()
time.sleep(2)
print("The End of an application")
print()

#Rule-2
print("===Rule-2===")
print()
print("Example-2")
import time
_12345=9999
print("The value is:",_12345)
print()
print("Address is:",id(_12345))
print()
print("datatype is",type(_12345))
print()
time.sleep(2)
print("The End of an application")
print()

#Rule-2
print("===Rule-2===")
print()
print("Example-3")
import time
a12345=9999
print("The value is:",a12345)
print()
print("Address is:",id(a12345))
print()
print("datatype is",type(a12345))
print()
time.sleep(2)
print("The End of an application")
print()

#Rule-2
print("===Rule-2===")
print()
print("Example-4")
import time
data_12345=9999
print("The value is:",data_12345)
print()
print("Address is:",id(data_12345))
print()
print("datatype is",type(data_12345))
print()
time.sleep(2)
print("The End of an application")
print()


#Rule-2
print("===Rule-2===")
print()
print("Example-5")
import time
____12345=9999
print("The value is:",____12345)
print()
print("Address is:",id(____12345))
print()
print("datatype is",type(____12345))
print()
time.sleep(2)
print("The End of an application")
print() 


#Rule-3 There is no lenght limit for a variable

print("===Rule-3===")
print()
print("Example-1")
import time
AAA=9999
print("The value is:",AAA)
print()
print("Address is:",id(AAA))
print()
print("datatype is",type(AAA))
print()
time.sleep(2)
print("The End of an application")
print()

#Example-2
print("Example-2")
print()
import time
__________=87967
print("The value is:",__________)
print()
print("Address is:",id(__________))
print()
print("datatype is",type(__________))
print()
time.sleep(2)
print("The End of an application")
print() 

#Rule-4 Python variables are case sensitive and case in_sensitive

#Case Sensitive = Case Sensitive can be represent as if the addresses of a variable are different 

print("===Rule-4===")
print()
print("Example-1")
import time
A=1000
B=2000
print("====Values are====")
print(A," ",B)
print()
print("===Addresses are===")
print(id(A)," ",id(B))
time.sleep(2)
print("The End of an application")
print()


#Case in_sensitive= Case in_sensitive can be represented if the address of the variable  is same
print("Rule-4")
print()
print("Example-2")
import time
A=1000
A=2000
A=3000
A=4000
A=5000
print("The Value is:",A)
print()
print("The Address is",id(A))
print()
print("Data type is:",type(A))
print()
time.sleep(3)
print("The End of an application")
print()



print("Example-3")
import time
A=1000
B=1000
C=1000
print("The Values are:",A,B,C)
print()
print("The Addresses are",id(A),id(B),id(C))
print()
print("Data type is:",type(A),type(B),type(C))
print()
time.sleep(3)
print("The End of an application")
print()  

import keyword
print(keyword.kwlist)

'''#Rule-5 An identifier are variable should not start with a reserve keyword,there are 35 reserve keywords in python programming language

import time
True=9000
False=1000
None=5555
print("Value is",True,False,None)
print()
print("Address is",id(True),id(False),id(None))
print()
print("datatype is",type(True),type(False),type(None))
print()'''