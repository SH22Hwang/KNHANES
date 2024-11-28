num = int(input())

paint_list = []  # 3차원
for i in range(num):
    p = []  # 2차원
    for _ in range(5):
        line = list(input())  # 1차원
        p.append(line)  # 2차원에 1리스트 추가

    paint_list.append(p)  # 3차원에 2리스트 추가
    print(f"{i}번째 그림")
    print(paint_list)
    print("#" * 10)
