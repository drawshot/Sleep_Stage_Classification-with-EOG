# 경로상에 있는 edf 파일 모두를 csv 파일을 이용하여 스테이지별로 wav 파일화 시키기 위한 파이썬 코드
# edf + csv -> wav file
# signal_number 변수 설정 : 신호의 이름 설정
# stage_path 리스트 변수 설정 : 생성할 wav 파일의 경로 설정
# 30초 단위로 wav 파일 생성

import pyedflib
import numpy as np
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
from scipy.io import wavfile
import csv
import os

signal_number = 0       # wav 파일로 변환하기 위한 신호 이름에 해당하는 리스트 인덱스 변수
fields_num = 0          # 시간에 해당하는 리스트 인덱스 변수

bef_bf = 0      # wav파일로 만들기 위한 시작 지점 초기화
aft_bf = 0      # wav파일로 만들기 위한 끝 지점 초기화
stage_name = ['WW', 'S1', 'S2', 'S3', 'S4', 'RR']   # 생성할 wav 파일의 분류명(스테이지 이름)
stage_path = ['WW_dataset/', 'S1_dataset/', 'S2_dataset/', 'S3_dataset/', 'S4_dataset/', 'RR_dataset/']     # 생성할 wav 파일의 마지막 경로 설정
stage_index = [1, 1, 1, 1, 1, 1]        # wav파일의 number를 저장(인덱스는 스테이지를 지칭)
stage_name_str = ['','','','','','']    # wav파일의 number 글자 길이를 위한 변수

name_max_index = 5      # 저장될 wav파일의 number 크기 설정(ex:00001)
name_before_number = ""     # wav파일의 number에서 0의 갯수 저장(ex:0000)
name_str = ""       # wav파일의 sleep stage string을 저장(ex:RR, WW, S1, S2, S3, S4)

edf_file_names = os.listdir('./edf_data/')      # 불러올 edf 파일의 이름을 저장(리스트 형식)
csv_file_names = os.listdir('./csv_data/')      # 불러올 csv 파일의 이름을 저장(리스트 형식)
# print(edf_file_names)
# print(csv_file_names)
# print(len(edf_file_names))

# 경로상에 존재하는 edf 파일의 갯수만큼 for 루프
for file_num in range(len(edf_file_names)) :

    f = pyedflib.EdfReader("data/" + edf_file_names[file_num])
    n = f.signals_in_file
    signal_labels = f.getSignalLabels()
    print(signal_labels)

    with open('csv_data/' + csv_file_names[file_num], 'r') as reader:
        for line in reader:
            fields = line.split(',')
            for i in range(len(fields)):
                if fields[i] == "30":
                    fields_num = i
                    break

    for a in range(len(signal_labels)):
        if signal_labels[a] == "Fp2-F4" or signal_labels[a] == "F2-F4":
            signal_number = a
            break

    sigbufs = np.zeros((n, f.getNSamples()[signal_number]))
    # print(f.getNSamples()[1])
    # print(sigbufs)
    sample_rate = f.getSampleFrequencies()[signal_number]
    # print(sample_rate)
    signal_bufs = f.readSignal(signal_number)

    # print(edf_file_names[file_num]," = ", fields_num, signal_number)

    with open('csv_data/' + csv_file_names[file_num], 'r') as reader:
        for line in reader:
            fields = line.split(',')
            # print(csv_file_names[file_num], fields_num)
            if fields[fields_num] == '30':
                aft_bf += sample_rate * 30
                signal = signal_bufs[bef_bf:aft_bf]
                bef_bf = aft_bf

                # if len(signal) == 15360 : continue
                # else : print(csv_file_names[file_num])

                if fields[0] == 'W':
                    stage_name_str[0] = str(stage_index[0])
                    for i in np.arange(name_max_index - len(stage_name_str[0])):
                        name_before_number += "0"

                    write(stage_path[0] + stage_name[0] + '_' + name_before_number + stage_name_str[0] + '.wav',
                          sample_rate, signal)
                    stage_index[0] += 1
                    name_before_number = ""

                elif fields[0] == 'S1':
                    stage_name_str[1] = str(stage_index[1])
                    for i in np.arange(name_max_index - len(stage_name_str[1])):
                        name_before_number += "0"

                    write(stage_path[1] + stage_name[1] + '_' + name_before_number + stage_name_str[1] + '.wav',
                          sample_rate, signal)
                    stage_index[1] += 1
                    name_before_number = ""

                elif fields[0] == 'S2':
                    stage_name_str[2] = str(stage_index[2])
                    for i in np.arange(name_max_index - len(stage_name_str[2])):
                        name_before_number += "0"

                    write(stage_path[2] + stage_name[2] + '_' + name_before_number + stage_name_str[2] + '.wav',
                          sample_rate, signal)
                    stage_index[2] += 1
                    name_before_number = ""

                elif fields[0] == 'S3':
                    stage_name_str[3] = str(stage_index[3])
                    for i in np.arange(name_max_index - len(stage_name_str[3])):
                        name_before_number += "0"

                    write(stage_path[3] + stage_name[3] + '_' + name_before_number + stage_name_str[3] + '.wav',
                          sample_rate,
                          signal)
                    stage_index[3] += 1
                    name_before_number = ""

                elif fields[0] == 'S4':
                    stage_name_str[4] = str(stage_index[4])
                    for i in np.arange(name_max_index - len(stage_name_str[4])):
                        name_before_number += "0"

                    write(stage_path[4] + stage_name[4] + '_' + name_before_number + stage_name_str[4] + '.wav',
                          sample_rate,
                          signal)
                    stage_index[4] += 1
                    name_before_number = ""

                else:
                    stage_name_str[5] = str(stage_index[5])
                    for i in np.arange(name_max_index - len(stage_name_str[5])):
                        name_before_number += "0"

                    write(stage_path[5] + stage_name[5] + '_' + name_before_number + stage_name_str[5] + '.wav',
                          sample_rate,
                          signal)
                    stage_index[5] += 1
                    name_before_number = ""

    bef_bf = 0
    aft_bf = 0

