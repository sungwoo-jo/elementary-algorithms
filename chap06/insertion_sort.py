# 단순 삽입 정렬 알고리즘 구현하기

from typing import MutableSequence

def insertion_sort(a:MutableSequence) -> None:
    """단순 삽입 정렬"""
    n = len(a) # 배열의 길이를 담아줌
    for i in range(1, n): # 1에서 n-1까지 순회
        j = i # j에 i를 담아줌 (i는 1에서 n-1까지)
        tmp = a[i] # tmp에 a[i]번째를 담아줌 (a[i]번째는 두번째 원소부터 n-1번째 원소까지
        while j > 0 and a[j - 1] > tmp: # j가 0보다 크고, a[j-1]번째 원소가 tmp보다 클때 동안 진행(계속 스캔해야 하는 조건)
            a[j] = a[j - 1] # 왼쪽 원소를 선택한 원소의 자리에 담아줌
            j -= 1 # 왼쪽으로 1칸 이동
        a[j] = tmp


if __name__ == "__main__":
    print("단순 삽입 정렬을 수행합니다.")
    num = int(input("원소 수를 입력하세요.: "))
    x = [None] * num # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f"x[{i}]: "))

    insertion_sort(x) # 배열 x를 단순 삽입 정렬

    print("오름차순으로 정렬했습니다.")
    for i in range(num):
        print(f"x[{i}] = {x[i]}")