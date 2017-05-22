v = [0 for i in range(1010)]
def BFS(a):
    Q = [a]
    v[a]=1
    while len(Q):
        a = Q.pop(0)
        print a,
        for i in range(len(E[a])):
            if v[E[a][i]]==0:
                v[E[a][i]]=1
                Q.append(E[a][i])
def DFS(a):
    print a,
    v[a] = 1
    l = len(E[a])
    for i in range(l):
        if v[E[a][i]]==0:
            DFS(E[a][i])
E = [[] for i in range(1010)]
n,m,st=map(int,raw_input().split())
for i in range(m):
    a,b=map(int,raw_input().split())
    E[a].append(b)
    E[b].append(a)
for i in range(1,n+1):
    E[i].sort()
DFS(st)
print ''
for i in range(n+1):
    v[i]=0
BFS(st)