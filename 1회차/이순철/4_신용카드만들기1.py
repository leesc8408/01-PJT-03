import sys

sys.stdin = open("_신용카드만들기1.txt")

T = int(input())
for test_case in range(1, T + 1):
    card_ = list(map(int, input().split()))
    # print(card_)
    cnt = []
    for i in range(len(card_)):
        if i % 2 == 0:
            cnt.append(card_[i] * 2)
        else:
            cnt.append(card_[i])
    n = sum(cnt) % 10
    if n == 0:
        print(f'#{test_case} {n}')
    else:
        print(f'#{test_case} {10-n}')