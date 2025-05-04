# W.A.P to show method overloading.
def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print(add(22,33))
print(add(34,45,88))
print(add(3))