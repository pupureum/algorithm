from itertools import product

def solution(word):
    words = []
    alpha = ['A', 'E', 'I', 'O', 'U']
    for i in range(1, 6):
        for j in product(alpha, repeat=i):
            words.append(''.join(list(j)))
    words.sort()
    return words.index(word) + 1