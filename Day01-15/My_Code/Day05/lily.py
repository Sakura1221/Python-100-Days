"""
找出100~999之间的所有水仙花数
水仙花数是各位立方和等于这个数本身的数
如: 153 = 1**3 + 5**3 + 3**3
"""
import time

start1 = time.perf_counter()
for num in range(100, 1000):
    a, b, c = map(int, str(num)) # 等价于 a,b,c = (int(i) for i in str(num))
    if num == a ** 3 + b ** 3 + c ** 3:
        print(num)
elapsed1 = time.perf_counter() - start1

start2 = time.perf_counter()
for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100 % 10
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)
elapsed2 = time.perf_counter() - start2

print(elapsed1,elapsed2)

### 第一个算法方便但是慢，第二个方法更好
### a = 12345，取个位(a // 1) % 10，取十位(a // 10) % 10，取百位(a // 100) % 10