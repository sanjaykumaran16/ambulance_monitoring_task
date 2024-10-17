import random,time,os
s=int(time.time_ns())+os.getpid()
random.seed(s)
a=random.randint(1,6)
print("Die lands on",a)
