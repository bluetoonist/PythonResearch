
# 사이킷 런을 이용한 메모리 사용량 예측 프로젝트
import csv
import psutil
import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression

model = LinearRegression()
train_save_path = "./train_set.csv"

# 데이터 수집 프로세스
# 총 100회
# 총 프로세스 수, 쓰레드 수, 메모리 사용량 예측 모델  train 수집
def data_collect_func():
    for _ in range(0, 2000):
        file_open_obj = open(train_save_path, "a+", newline='')
        write_row = csv.writer(file_open_obj)

        # 전체 프로세스 수집
        tot_process_number = len(list(_ for _ in psutil.pids()))
        # 전체 쓰레드 수집
        tot_thread_number = sum([_.num_threads() for _ in psutil.process_iter()])
        # 메모리 사용량 수집
        memory_usage = psutil.virtual_memory().percent

        # train Dat Create filez
        write_row.writerow([tot_process_number, tot_thread_number, memory_usage])
        print("데이터 수집 횟수 : [", _, "]")

def linear_predict_func():
    # 선형회귀 모델 예측하기
    _dataset = pd.read_csv(train_save_path, names=['process', 'threads', 'memory_usage'], sep=",")

    _train_process = _dataset["process"].to_numpy()
    _train_threads = _dataset["threads"].to_numpy()
    _train_memory = _dataset["memory_usage"].to_numpy()

    train_data_merge = np.dstack([_train_process[0::], _train_threads[0::]])
    two_degree_trans = train_data_merge[0]

    lin_reg = LinearRegression()
    lin_reg.fit(two_degree_trans, _train_memory)

    # predict value
    for x in range(1, 100):
        # 전체 프로세스 수집
        tot_process_number = len(list(_ for _ in psutil.pids()))
        # 전체 쓰레드 수집
        tot_thread_number = sum([_.num_threads() for _ in psutil.process_iter()])
        # 현제 메모리 사용량
        memory_usage = psutil.virtual_memory().percent

        predict = lin_reg.predict([[tot_process_number, tot_thread_number]])
        print("Current Memory", memory_usage, "============== Predict :", predict, )

if __name__ == '__main__':
    print("\n 메모리 사용량 예측 " )
    print("\n 1.데이터 수집(1000회)")
    print("\n 2.사이킷 런 선형회귀 (100회) ")

    choice_number = int(input("번호 선택: "))

    if (choice_number == 1):
        data_collect_func()
    elif (choice_number ==2):
        linear_predict_func()
    else:
        exit()