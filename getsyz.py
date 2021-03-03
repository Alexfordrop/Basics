import sys

sys.getsizeof(5)
sys.getsizeof(range(0, 10000))
sys.getsizeof([1, 2, 'c'])

print(sys.getsizeof(5))
print(sys.getsizeof(range(0, 10000)))
print(sys.getsizeof([1, 2, 'c']))