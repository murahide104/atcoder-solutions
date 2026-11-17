# s = input()

# flag = True

# if len(s) % 2 == 1:
#     flag = False

# if flag:
#     check_cnt = [0]*26
#     for i in range(len(s) // 2):
#         if s[i*2] != s[i*2+1]:
#             flag = False
#             break
        
#         check_cnt[ord(s[i*2]) - ord('a')] += 2
#         if check_cnt[ord(s[i*2]) - ord('a')] > 2:
#             flag = False
#             break

# print("Yes" if flag else "No")

s = input()

flag = True

if len(s) % 2 == 1:
    flag = False

if flag:
    for i in range(0, len(s), 2):
        if s[i] != s[i+1]:
            flag = False
            break

if flag:
    if len(set(s)) != len(s) // 2:
        flag = False

print("Yes" if flag else "No")