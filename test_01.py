import copy

def add(a):
    c = copy.deepcopy(a)
    c[2].append(5)

    print(
        id(c)
    )

    print(c)

    for i in c:
        print(i)
    


b = [1, 2, [3, 4]]
print(
    id(b)
)

print(b)

print(
    add(b),
)

print(b)