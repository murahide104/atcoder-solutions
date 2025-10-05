n, q = map(int, input().split())
cnt = [0] + [1] * n
next = list(range(n + 2))

def find(v):
    while next[v] != v:
        next[v] = next[next[v]]
        v = next[v]
    return v

out = []
for _ in range(q):
    X, Y = map(int, input().split())
    upgraded = 0
    v = find(1)
    while v <= X:
        upgraded += cnt[v]
        cnt[Y] += cnt[v]
        cnt[v] = 0
        next[v] = find(v + 1)
        v = find(v)
    out.append(str(upgraded))
print("\n".join(out))