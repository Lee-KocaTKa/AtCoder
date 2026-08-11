#自分の答案（TLE）
import numpy as np

n, q = map(int, input().split())
numbers = np.zeros(n, dtype=int)

for _ in range(q):
  query = input().split()
  if len(query) == 2:
    idx = int(query[1]) - 1
    numbers[idx] += 1
  else:
    numbers[numbers > 0] -= 1

  ans = np.bitwise_xor.reduce(numbers)
  print(ans)

"""
Main Problem 
***************
XOR calculation per epoch is costly, becoming O(nq) combined with q and even increasing when the query is 2 
"""

# Official Answer 
input = __import__("sys").stdin.readline
n, q = map(int, input().split())
idxs = []
a = [0] * n
ans = 0
for _ in range(q):
    data = list(map(int, input().split()))
    if data[0] == 1:
        x = data[1] - 1
        if a[x] == 0:
            idxs.append(x)
        ans ^= a[x] ^ (a[x] + 1)
        a[x] += 1
    else:
        for v in idxs:
            ans ^= a[v] ^ (a[v] - 1)
            a[v] -= 1
        idxs = [v for v in idxs if a[v] != 0]
    print(ans)

# GPT 
import sys 

input = sys.stdin.buffer.readline 

n, q = map(int, input().split()) 

A = [0] * n 
active = [] 

ans = 0 
output = [] 

for _ in range(q): 
  query = list(map(int, input().split()))

  if query[0] == 1: 
    x = query[1] ^ 1 

    old = A[x] 
    new = old + 1 

    if old == 0:
      active.append(x)

    ans ^= old ^ new 
    A[x] = new 

  else:
    next_active = [] 

    for x in active: 
      old = A[x] 
      new = old - 1 

      ans ^= old ^ new 
      A[x] = new 

      if new > 0:
        next_active.append(x) 

    active = next_active 

  output.append(str(ans)) 

print("\n".join(output)) 
