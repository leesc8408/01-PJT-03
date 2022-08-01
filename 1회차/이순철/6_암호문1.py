from posixpath import split
import sys

sys.stdin = open("_암호문1.txt")

for test_case in range(1, 11):
    amho_len = int(input())
    amho = input().split()
    mi_len = int(input())
    mi_list = list(input().split())
    print(amho_len)
    print(amho)
    print(mi_len)
    print(mi_list)
