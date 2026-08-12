# 自分の答案
import math 

A, B = list(map(int, input().split())) 


if A >= B:
  if B == 1:
    print(0)
  else:
    print(1) 
else: 
  diff = B - A
  augment = A - 1
  more_strips = math.ceil(diff / augment)
  print(more_strips + 1)

# GPT
"""
point : in one line,
1 + k(A - 1) >= B
so,
k >= (B - 1) / (A - 1)

plus, it's advisable to avoid floats
so,
ceil(x / y) is better expressed as 
(x + y - 1) // y 
"""
A, B = map(int, input().split())

need = B - 1
gain = A - 1

ans = (need + gain - 1) // gain
print(ans)
