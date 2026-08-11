# 自分の答案
n = int(input())

for i in range(n):　# Rather, range(1, n+1) better 
  j = i + 1
  if j%3 == 0:
    print("Fizz")
  else:
    print(j)


# GPTの答案
n = int(input())

for i in range(1, n + 1):
    print("Fizz" if i % 3 == 0 else i)  # spaces around the operator 
