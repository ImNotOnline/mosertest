import math
def log2(x):
    return (math.log10(x) / math.log10(2));
def moser(x):
    y = (1 + math.comb(x,2) + math.comb(x,4))
    z = log2(y)
    if z % 1 == 0:
        print(str(x) + ", 2^" + str(z))
    elif log2(x) % 1 == 0:
        print(str(x) + ", failure")
x = 0
while True:
    x+= 1
    moser(x)
