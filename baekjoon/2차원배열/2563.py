def square(x,y,N):
    for i in range(x,x+10):
        for j in range(y,y+10):
            N[j][i] = 1
    return N

b = int(input())
bb = 0
N = [[0] * 100 for _ in range(100)]
c = [[0] * 100 for _ in range(100)]

for _ in range(b):
   x,y = map(int,input().split())
   N = square(x,y,N)

for i in range(100):
    for j in range(100):
        if N[i][j] ==1:
            bb += 1
print(bb)
