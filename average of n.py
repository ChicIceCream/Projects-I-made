from typing import List


print("How many numbers you want to get an average of? : ")
n = int(input())
result = 0
for i in range(n):
    i = int(input())
    result += i

print(result/n)