def perf(n:int):
    div = []
    for i in range(1,n):
        if n%i == 0: div.append(i)

    if sum(div) == n: div.append(1)
    else: div.append(0)
    return div

n = 1
while True:
    n = int(input())
    if n == -1: break
    p = perf(n)
    if p[-1]:
        q = list(map(str,p[:-1]))
        print(n,"="," + ".join(q))
    else: print(n,"is NOT perfect.")
