from typing import MutableSequence

def shaker_sort(a: MutableSequence) -> None:
    """셰이커 정렬"""
    left = 0
    right = len(a) - 1
    last = right
    while left < right: # 오른쪽이 왼쪽보다 큰 경우 교환
        for j in range(right, left, -1): # 원소를 맨 뒤에서 맨 앞으로 스캔
            if a[j - 1] > a[j]: # 앞의 값이 뒤보다 큰 경우에 교환
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j # 가장 작은 원소를 last에 저장
        left = last # left에 last(가장 작은 원소)를 저장

        for j in range(left, right): # 원소를 맨 앞에서 맨 뒤로 스캔
            if a[j] > a[j + 1]: # 앞의 값이 뒤보다 큰 경우에 교환
                a[j], a[j + 1] = a[j + 1], a[j]
                last = j # 가장 작은 원소를 last에 저장
        right = last # right에 last(가장 작은 원소)를 저장

if __name__ == "__main__":
    print("버블 정렬을 수행합니다.")
    num = int(input("원소 수를 입력하세요.: "))
    x = [None] * num # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f"x[{i}]: "))

    shaker_sort(x) # 배열 x를 버블 정렬

    print("오름차순으로 정렬했습니다.")
    for i in range(num):
        print(f"x[{i}] = {x[i]}")