class Numbers:
    def __init__(self,n):
        self.n=n
        self.current=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current<=self.n:
            num=self.current
            self.current+=1
            return num
        raise StopIteration
for i in Numbers(5):
    print(i)


nums=[1,2,3,4,5]
evens=iter([x for x in nums if x%2==0])
for i in evens:
    print(i)

class Reverse:
    def __init__(self,text):
        self.text=text
        self.index=len(text)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index==0:
            raise StopIteration
        self.index-=1
        return self.text[self.index]
for ch in Reverse("hello"):
    print(ch)

def with_index(lst):
    i=0
    while i<len(lst):
        yield i
        yield lst[i]
        i+=1
for val in with_index([10,20,30]):
    print(val)

def digits(num):
    for d in str(num):
        yield int(d)
for i in digits(12345):
    print(i)


def cumulative(lst):
    total=0
    for i in lst:
        total+=1
        yield total
for i in cumulative([1,2,3]):
    print(i)


def vowels(text):
    for ch in text:
        if ch.lower() in "aeiou":
            yield ch
for i in vowels("education"):
    print(i)

def words(sentence):
    for word in sentence.split():
        yield word
for w in words("python is easy"):
    print(w)


def even_chars(text):
    for i in range(0,len(text),2):
        yield text[i]
for ch in even_chars("abcdef"):
    print(ch)


def running_max(lst):
    m=lst[0]
    for i in lst:
        if i>m:
            m=i
        yield m
for i in running_max([3,1,4,2]):
    print(i)