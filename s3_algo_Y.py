a = {}
b = dict(short='dict', long='dictionary')
print(b)
d = {a: a ** 2 for a in range(7)}
print(d)

print(a.get(2))

d2 = {"A1":"123", "A2":"456"}
print("A1" in d2)
print("A3" in d2)
print(d2.keys())
print(d2.popitem())