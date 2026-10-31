x = 5
if (type(x) is int):
    print("true")
else:
    print("false")

x = 5.5
if (type(x)is not float):
    print("true")
else:
    print("false")

x = 20
y = 30
y = 30 - 10
if (x is y):
    print("x & y SAME identity")

y = 30
if (x is not y):
    print("x & y have DIFFERENT identity")

