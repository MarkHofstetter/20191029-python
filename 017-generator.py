def float_range(low, high, step):
    current = low
    while current <= high:
        yield current
        current += step

def fibonaci(end):
    c1 = 1
    c2 = 1
    current = c1
    yield current    
    while current <= end:
        yield current
        current = c1 + c2
        c1 = c2
        c2 = current               
    
for i in float_range(2,4,0.1):
    print(i)

for f in fibonaci(40):
    print(f)