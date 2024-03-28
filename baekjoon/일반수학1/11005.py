#진법 변환 2 -> 나머지는 뒤에서부터 해야한다. ! 앞에서부터가 아니다.
a,b = map(int,input().split())
z = []
zz = list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
while(a!=0):
        c = a//b
        cc = a%b
        z.append(cc)
        a = c
z = z[::-1]
for i in z:
    print(zz[i],end = "")