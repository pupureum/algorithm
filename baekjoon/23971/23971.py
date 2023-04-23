h, w, n, m = map(int, input().split())

import math
row = math.ceil(h / (n + 1))
col = math.ceil(w / (m + 1))
print(col * row)