---
title: "3-1) 파이썬의 주요 내장 객체 : 네이버 카페"
source: "https://cafe.naver.com/f-e/cafes/25331457/articles/19018?boardtype=L&menuid=304&referrerAllArticles=false"
author:
published:
created: 2026-06-23
description:
tags:
  - "clippings"
---

# %% normal calculization
a = 5
b = 2

print(a + b)   # 7
print(a // b)  # 2
print(a % b)   # 1
print(5 ** 2)

# %% Compare Calculator
print(5 > 3)      # True
print(5 == 3)     # False

# %% and or not calculator
print(True and False)   # False
print(True or False)    # True
print(not True)         # False

# %% Membership Calculator
print(3 in [1, 2, 3])       # True
a = [1, 2, 3]
print(4 in a)  # False
print(4 not in a)   # True
# %% distinguishioin Calculator
a = [1, 2]
b = a

a is b      # True
a == b      # True
c = [1, 2]
d = [1, 2]

c is d      # False
c == d      # True
print(c is d)
print(c == d)

# %% Triple Calculator
score = 50
result = "합격" if score >= 60 else "불합격"
print(result)

# %% Substitution Calculator
a = 10

# a = a+ 5와 같은 표현(편한거 사용하면 된다)
a += 5
print(a)  # 15

# %% Wallus Calculator
n = 10
result = (x := n>5)   # 대입하면서 값
# initial version of Python was unavailable to use replace (wallus) execution method. by that they made these method to use replace Calculator
print(result)
