n,m = map(int, input().split())
basket = [i for i in range(1,n+1)]
for i in range(m):
    i,j = map(int,input().split())
    k = basket[i-1:j]
    basket[i-1:j] = k[::-1]
for j in basket:
    print(j,end=' ')
