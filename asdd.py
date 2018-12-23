import random
import time
q1 = int(input("5"))
time.sleep(1)
w1 = int(input("4"))
time.sleep(1)
e1 = int(input("3"))
time.sleep(1)
r1 = int(input("2"))
time.sleep(1)
t1 = int(input("1"))
time.sleep(1)

q = random.radint(1,49)
w = random.radint(1,49)
e = random.radint(1,49)
r = random.radint(1,49)
t = random.radint(1,49)
if q == q1 and w == w1 and e == e1 and r == r1 and t == t1:
        print("100000000 LİRA KAZANDIN")
		
                        
if q != q1 and w == w1 and e == e1 and r == r1 and t == t1:
        print("1000000")

                        
if q != q1 and w != w1 and e == e1 and r == r1 and t == t1:
        print("13213")
	
if q != q1 and w != w1 and e != e1 and r == r1 and t == t1:
        print("3131")
		
                        
if q != q1 and w != w1 and e != e1 and r != r1 and t == t1:
        print("1")
		
                        
if q != q1 and w != w1 and e != e1 and r != r1 and t != t1:
        print("kaybettin")
									


time.sleep(10)
