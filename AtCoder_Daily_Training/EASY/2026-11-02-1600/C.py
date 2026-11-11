# from collections import Counter

# total_count_color = int(input())
# colors = list(map(int, input().split()))
# max_count_color = Counter(colors).most_common(1)[0][1]
# print(total_count_color - max_count_color)

from collections import Counter

ball_count = int(input())
colors = list(map(int, input().split()))
max_color_count = Counter(colors).most_common(1)[0][1]
print(ball_count - max_color_count)