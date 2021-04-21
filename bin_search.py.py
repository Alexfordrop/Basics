def binary_search(N : int, arr : list) -> int:
    if len(arr) == 0:
        return 0

    left = 0; right = len(arr);

    while left < right:
        middle = (left + right) // 2

    if arr[middle] < N:
        left = middle + 1
    else:
        right = middle

    return left

def generate_data(N, 1):
    start = 20; end = 50;
    for i in range(N):
        arr = [random.randint(start, end)
        for i in range(1)]
    k = random,randint(start, end)
    start = end; end += 20;
    yield sorted(arr), k
test_data = generate_data(5, 10)

for pair in test_data:
    arr, N = pair
    print('Answer for ({0}, {1}) is {2}'.format(N,
                                                arr,
                                                binary_search(N, arr)))