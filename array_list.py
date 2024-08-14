## 함수 선언 부분 ##
def add_data(element):
    list.append(None)
    len_list = len(list)
    list[len_list - 1] = element

# 선형 리스트에 데이터를 삽입하는 함수
def insert_data(position, element):
    if position < 0 or position > len(list):
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return

    list.append(None)  # 빈칸 추가
    len_list = len(list)   # 배열의 현재 크기

    for i in range(len_list - 1, position, -1):
        list[i] = list[i - 1]
        list[i - 1] = None

    list[position] = element    # 지정한 위치에 친구 추가

# 선형 리스트에서 데이터를 삭제하는 함수
def delete_data(position):
    if position < 0 or position > len(list):
        print("데이터를 삭제할 범위를 벗어났습니다.")
        return

    len_list = len(list)
    list[position] = None  #데이터 삭제

    for i in range(pos, len_list-1):
        list[i] = list[i+1]
        list[i+1] = None     # 배열의 맨 마지막 위치 삭제

    del(list[len_list - 1])

## 전역 변수 선언 부분 ##
list = []
select = -1     # 1: 추가, 2: 삽입, 3: 삭제, 4: 종료

## 메인 코드 부분 ##
if __name__ == "__main__":
    while(select != 4):
        select = int(input("선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)--> "))

        if (select == 1):
            data = input("추가할 데이터--> ")
            add_data(data)
            print(list)
        elif (select == 2):
            pos = int(input("삽입할 위치--> "))
            data = input("추가할 데이터--> ")
            insert_data(pos, data)
            print(list)
        elif (select == 3):
            pos = int(input("삭제할 위치--> "))
            delete_data(pos)
            print(list)
        elif (select == 4):
            print(list)
            exit
        else:
            print("1~4 중 하나를 입력하세요.")
            continue
