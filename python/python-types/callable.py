from typing import Callable

SumThreeFunction = Callable[[int], int]

def compute_stats(users, plans, products):
    ...

def multiply_by_two(x: float) -> float: # Just to see the error type float in the add_three atribution
    return x * 2.0  

def add_three(x: int) -> int:
    return x + 3


add_three_fn: SumThreeFunction = add_three
print(add_three_fn(3)) # Should return 6

