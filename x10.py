a=int(input())
b=int(input())
for i in range(a,b+1):
    if i==1:
        continue
    y=1
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            y+=j
            if j*j != i//j:
                y += i//j
    if y==i:
        print(i,end=" ")
