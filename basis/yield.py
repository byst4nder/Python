#! python3
# 了解yield特性
import random

def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:", res)


def fooA():
    print("starting...")
    res = 4
    print("res:", res)


g = foo()
print(next(g))
print("*"*20)
print(next(g))
print("*"*60)
print(g.send(20))
print(next(g))
print("*"*60)
#m = fooA()
# print(m)


def foo(num):
    print("starting...")
    while num < 10:
        num = num+1
        yield num


# lst=list(foo(0))
m = foo(0)
print(next(m))
print(next(m))


def randomnum():
    while True:
        yield   random.randint(1,100000)


print(list(randomnum().__next__() for num in range(1,100)))
    

        

#lst=list(randomnum(10))         

