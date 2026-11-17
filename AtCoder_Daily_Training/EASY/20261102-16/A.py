# n = int(input())
# s = input()

# answer = ""

# for char in s:
#     answer += char*2

# print(answer)

n = int(input())
s = input()

print("".join(c*2 for c in s))