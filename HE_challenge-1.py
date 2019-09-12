a, b, c = [int(i) for i in input().split(' ')]
def code(a, b, c):
    a, b = b, a
    a = a*c
    b = b + c
    print(a, b, sep = ' ')

code(a, b, c)