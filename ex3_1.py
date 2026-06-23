# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: title,-all
#     formats: py:percent,ipynb
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
# ---

# %%
# 파이썬의 숫자는 "정수"와 소수 부분이 있는 "부동 소수점 수"를 제공한다.

# %%
# 1. 정수 (int)
a = 10
print(a)
print(type(a))


# %%
# 2. 실수 (float)
b = 3.14
print(b)
print(type(b))

# %%
# 3. 복소수 (complex)
c = 3 + 4j
print(c)
print(type(c))

# %%
# 4. 논리값 (bool)
d = True
print(d)
print(type(d))

# %%
# 5. 문자열 (str)
e = "Python"
print(e)
print(type(e))

# %%
# 6. 리스트 (list)
f = [1, 2, 3]
print(f)
print(type(f))

# %%
# 7. 튜플 (tuple)
g = (1, 2, 3)
print(g)
print(type(g))

# %%
# 8. 딕셔너리 (dict)
h = {"a": 1}
h = {"id": "admin", "pw": "1234"}
h = {"id": "admin", (1, 3, 5, 6): "1234"}
print(h)
print(type(h))

print(h["id"])
print(h)
## almost every 80% of variable datas are usally Dict & Tuple

# %%
# 9. 집합 (set)
i = {1, 2, 3}
print(i)
print(type(i))

# print(i[0]) #error
i = {1, 2, 3, 3}  # same variable would be ignored
print(i)


# %%
# 10. 범위 (range)
j = range(5)
print(j)
print(type(j))
print(list(j))
j2 = list(j)
print(j2)
print(type(j2))

# %%
# 11. 바이트 (bytes)
k = b"abc"
print(k)
print(type(k))

# %%
# 12. 바이트배열 (bytearray)
l = bytearray(b"abc")
print(l)
print(type(l))

# %%
# 13. 없음 (NoneType)
m = None
print(m)
print(type(m))


# %%
# 14. 함수 (function)
def hello():
    print("Hello")
    print("bye")


print(hello)
print(type(hello))
hello()

a = 10
# a()
# TypeError: 'int' object is not callable

# %%
# 15. 모듈 (module)
import math

print(math)
print(type(math))


# %%
# 16. 클래스 (type)
class Person:
    pass


print(Person)
print(type(Person))

# %% 첫 번째 블록 (데이터 로드)
import numpy as np
import pandas as pd

print("데이터를 준비합니다.")

# %% 두 번째 블록 (간단한 계산)
data = np.array([1, 2, 3, 4, 5])
result = data * 2
print(result)

# %%
name = "KMove"  # KMove 라는 문자열 객체를 생성하고 반환된 문자열을 name이라는 변수에 대입(할당)
