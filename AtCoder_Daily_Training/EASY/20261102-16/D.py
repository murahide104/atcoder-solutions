test_case_count = int(input())

for _ in range(test_case_count):
    _number_count = int(input())
    numbers = list(map(int, input().split()))
    odd_count = sum(1 for number in numbers if number % 2 != 0)
    print(odd_count)