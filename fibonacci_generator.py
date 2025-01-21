def fibo_generator():
   a,b=0,1
   while True:
       yield a
       a ,b = b,a+b






re = fibo_generator()
for i in range(10):
    print(next(re))




# for i in range(9):
#      re = fibo_generator(i)
#      next(re)