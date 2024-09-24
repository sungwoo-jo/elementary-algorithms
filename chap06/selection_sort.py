# 단순 선택 정렬 알고리즘 구현하기

from typing import MutableSequence

def selection_sort(a: MutableSequence) -> None:
    """단순 선택 정렬"""
    n = len(a) # 배열의 길이 담아주기
    for i in range(n - 1): # 맨 뒤 원소는 자동으로 가장 큰 값이 남게 되기때문에 n - 1까지
        min = i # 매번 i를 min에 담아줌
        for j in range(i + 1, n): # i는 첫번째부터, j는 두번째부터 비교
            if a[j] < a[min]: # j번째 원소보다 min이 크다면
                min = j # j가 가장 작은 값이므로 min에 넣어줌
        a[i], a[min] = a[min], a[i] # 위치를 교환

if __name__ == "__main__":
    print("선택 정렬을 수행합니다.")
    num = int(input("원소 수를 입력하세요.: "))
    x = [None] * num # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f"x[{i}]: "))

    selection_sort(x) # 배열 x를 선택 정렬

    print("오름차순으로 정렬했습니다.")
    for i in range(num):
        print(f"x[{i}] = {x[i]}")