from functools import reduce


def dec(x):
    def inner():
        print("Start")
        x()
        print("End")
    return inner
@dec
def greet():
    print("Hello")
greet()

#2.question
def dec(x):
    def inner(name):
        print("start")
        x(name)
        print("done")
    return inner
@dec
def greet(name):
    print("hello",name)
greet("Ravi")


#3question
def dec(func):
    def inner():
        result = func()
        return result * 2
    return inner

@dec
def number():
    return 30
print(number())


#4.question
user_role="student"
def check(func):
    def inner():
        if user_role=="admin":
            func()
        else:
            print("access denied")
    return inner
@check
def show():
    print("welcome admin")
show()


#5.question
def upper(func):
    def inner():
        return func().upper()
    return inner
@upper
def get_msg():
    return "Hello world"
print(get_msg())

#lamda
a=[1,2,3,4]
b=[10,20,30,40]
result=list(map(lambda x,y:x+y,a,b))
print(result)

#3
num=[12,15,7,18,20,21,25]
result=list(filter(lambda x:(x%3==0)^(x%5==0),num))
print(result)

#4
num=[1,2,3,4]
result=reduce(lambda x,y:x+y,num,10)
print(result)

#5
num=[[1,2],[3,4],[5,6]]
result=list(map(lambda x:x.append(10),num))
print("Result:",result)
print("num:",num)



