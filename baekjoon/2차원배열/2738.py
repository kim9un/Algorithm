#행렬덧셈
#출력 방식이 잘못됐었다. print()는 한 줄 뛰는거
n,m = map(int,input().split())
a =[list(map(int,input().split())) for _ in range(n)]
b =[list(map(int,input().split())) for _ in range(n)]

c = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        c[i][j] = a[i][j] +b[i][j]

for i in range(n):
    for j in range(m):
        print(c[i][j], end=" ")
    print()
