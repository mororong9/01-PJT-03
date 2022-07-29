import sys

sys.stdin = open("_소득불균형.txt")

T = int(input())
income = []
total = 0

for test_case in range(1, T + 1):
    num = int(input())
    income = list(map(int, input().split()))
    income_avg = sum(income) / num
    cnt=0
    for c in income:
        if c <= income_avg:
            cnt += 1
    print(f'#{test_case} {cnt}')