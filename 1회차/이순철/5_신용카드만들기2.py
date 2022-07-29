import sys

sys.stdin = open("_신용카드만들기2.txt")

T = int(input())
for test_case in range(1, T + 1):
    card_no = input().split()
    for i in card_no:
        for j in i:
            print(j)