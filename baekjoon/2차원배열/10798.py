#try except로 빈 리스트에 넣는걸 생각하는게 오래걸렸음

a = [list(input()) for _ in range(5)]
b = 0
c = []
for i in a:
    if (len(i) > b):
        b = len(i)

for i in range(b):
    for j in range(5):
            try:
                c.append(a[j][i])
            except:
                c.append("*")

for i in c:
    if(i != "*"):
        print(i,end = "")