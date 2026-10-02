Example = [0,1,1,0,1,1,0,1]
"""

def a(y):
    for i in range(4):
        y[i] = 1
    return y

print(a(Example))
"""
"""
def c(y):
    for i in range(len(y)):
        if y[i] == 1:
            y[i] = 0
        else:
            y[i] = 1
    return y

print(c(Example))
"""
"""
Example_RGB = [1,1,1,0,1,0,1,1,0,1,0,0,0,1,0,0,1,1,1,1,0,0,1,1]

def h(y):
    for i in range(len(y)):
        y[i] = 1
    return y

print(h(Example_RGB))
"""