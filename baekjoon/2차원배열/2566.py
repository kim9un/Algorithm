#최댓값
#if문에서 >= 부등호에서 리스트가 int형보다 앞에 있어야 됨
def max(N):
    aa = 0
    row = 0
    col = 0
    for i in range(9):
        for j in range(9):
            if N[i][j] >= aa:
                aa = N[i][j]
                row = i+1
                col = j+1

    return aa,row,col

a = [list(map(int,input().split())) for _ in range(9)]
v,b,n = max(a)
print(v)
print(b,n,sep = " ")