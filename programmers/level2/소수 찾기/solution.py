import math
from itertools import permutations

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    data = [n for n in numbers]
    unit = []
    for k in range(1, len(numbers) + 1):
        unit += list(permutations(data, k))
    new_numbers = [int("".join(u)) for u in unit]
    for n in new_numbers:
        if n < 2:
            continue
        if is_prime_number(n):
            answer.append(n)
    return len(set(answer))

print(solution("17"))
print(solution("011"))