def no_negative(func):
    def inner(a,b):
        result=func(a,b)
        if result <0:
            return 0
        return result
    return inner
@no_negative
def subtract(a,b):
    return a-b
print(subtract(5,10))
print(subtract(10,5))
