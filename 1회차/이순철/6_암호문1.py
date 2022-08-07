import sys

sys.stdin = open("_암호문1.txt")

for test_case in range(1, 11):

    amho_len = int(input())
    amho = input().split()
    mi_len = int(input())
    mi_list = list(input().split())
    # print(mi_list)
    for i in range(len(mi_list)):
    # 암호문 리스트만큼 반복
        if mi_list[i] == 'I':
        # 'I'가 나오면 해당 인덱스 기준으로
            x = mi_list[i + 1]
            # x 값 삽입할 위치 
            y = mi_list[i + 2]
            # y 값 삽입 될 숫자의 갯수
            for j in reversed(range(int(y))):
            # 삽입 할 위치가 x 값 하나로 고정되므로 삽입 될 갯수만큼 인덱스를 더해서 역순으로 반복
                s = mi_list[i + 3 + j]
                # 삽입 숫자의 인덱스는 [기준(I) + x,y 다음 인덱스(3) + y값을 역순으로 반복한 값(j)] 
                amho.insert(int(x), s)
                # 원본 암호에 삽입 x위치에 s를 삽입 / y갯수 만큼 반복
    print(f'#{test_case} ', *amho[0:10])
    # 10자리만 출력하기위해 인덱스로 슬라이싱 출력
                