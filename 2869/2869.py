import math

A, B, V = map(int, input().split())

print(math.ceil(1 + (V - A) / (A - B)))