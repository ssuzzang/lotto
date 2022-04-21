import random
import numpy as np
import pandas as pd 
def read_data():
    df = pd.read_csv("lotto.csv", skiprows=1)
    lotto_number_list = []
    for row in range(len(df)):
        l = [df.values[row][1], df.values[row][2], df.values[row][3], df.values[row][4], df.values[row][5], df.values[row][6]]
        lotto_number_list.append(l)

    return lotto_number_list

# 빈도수를 기준으로 로또 번호를 뽑아주는 함수
def get_lotto_number_by_frequency():
  
    numbers = read_data()
    # 각 번호 별로 빈도수 체크
    count = np.zeros(45)
    for i in numbers:
        for j in i:
            count[int(j) - 1] += 1
    
    # 번호 당 나온 개수만큼 추가할 배열
    number_list = []

    # n: 로또 번호
    # j: 번호당 나온 수
    for n, j in enumerate(count):
        # j만큼 (n+1)한 값을 추가
        for i in range(int(j)):
            number_list.append(n + 1)

    # 섞어주고
    np.random.shuffle(number_list)
    lotto_number = []
    # 번호 여섯개 뽑기
    for i in range(6):
        idx = random.randint(0, len(number_list))
        selected_number = number_list[idx]
        lotto_number.append(selected_number)

        while selected_number in number_list:
            number_list.remove(selected_number)

    return(sorted(lotto_number))
     
def get_lotto(num):
  lotto_list = []
  for i in range(num):
    lotto_list.append(get_lotto_number_by_frequency())
  return lotto_list

    