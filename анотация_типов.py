from typing import List, Dict

numbers: Dict[str, int] = {'one': 1, 'two': 2}
values: List[int] = numbers.values()

def _sum(a: int, b: int) -> int:
    return a + b

_sum(*values)

_sum('Rock ', 'Hard')

print(_sum(*values))
print(_sum('Rock ', 'Hard'))