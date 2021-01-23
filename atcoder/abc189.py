words = list(input())

if words[0] == words[1] and words[1] == words[2]:
    print("Won")
else:
    print("Lost")

#2

n, max = map(int, input().split())
max = max * 100
count = 0
num = -1
alcohol = {}

for i in range(n):
    volume, percent = map(int, input().split())
    alcohol[i] = volume * percent

for j in range(n):
    count += alcohol[j]
    if count > max:
        num = j + 1
        break

print(str(num))

# 3
n = int(input())
orange = list(map(int, input().split()))
max = 0

for i in range(n):
    min = orange[i]
    for j in range(i, n):
        if orange[j] < min:
            min = orange[j]
        count = min * (j - i + 1)
        if count > max:
            max = count

print(str(max))

# 4
n = int(input())
s = {}
for i in range(n):
    s[i] = input()

def patternCount(n: int, s: list):
    if n == 0:
        return 1
        
    if s[n - 1] == 'AND':
        return patternCount(n - 1, s)
    else:
        return patternCount(n - 1, s) + pow(2, n)

print(str(patternCount(n, s)))
