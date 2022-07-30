import sys

sys.stdin = open("_암호문1.txt")

# for test_case in range(1, 11):
amho_len = int(input())
amho = {}
for i in range(amho_len):
    amho.append(input().split())
print(amho)
