# n = int(input())
# a = sorted(list(map(int, input().split())), reverse=True)
# b = sorted(list(map(int, input().split())), reverse=True)

# answer = a[-1]
# flag = False
# for i in range(n-1):
#     if a[i] > b[i]:
#         if flag:
#             print(-1)
#             exit()
#         b.insert(i, a[i])
#         answer = a[i]
#         flag = True
# else:
#     if flag and a[-1] > b[-1]:
#         print(-1)
#         exit()
#     print(answer)

n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)
b = sorted(list(map(int, input().split())), reverse=True)
b.append(0)

answer = -1
flag = False
for i in range(n):
    if a[i] > b[i]:
        if flag:
            print(-1)
            exit()
        b.insert(i, a[i])
        answer = a[i]
        flag = True

print(answer)