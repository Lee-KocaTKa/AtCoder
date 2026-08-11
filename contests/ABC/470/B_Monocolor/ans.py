# 自分の答案
n = int(input())
C = [int(i) for i in input().split()]
most_frequent = max(set(C), key=C.count)  # O n-square (NG)
cnt = 0
for i in C:
  if i != most_frequent:
    cnt += 1
print(cnt)


# GPTの答案其の一
from collections import Counter

n = int(input())
C = list(map(int, input().split()))

freq = Counter(C) # outputs a dictionary-shaped structure 

print(n - max(freq.values()))

# GPTの答案その二（Counter使わず）
n = int(input())
C = list(map(int, input().split()))

count = [0] * (n + 1)

for c in C:
    count[c] += 1

print(n - max(count))
