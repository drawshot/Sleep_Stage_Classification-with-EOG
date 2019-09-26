# 경로상에 있는 하나의 edf 파일을 csv 파일을 이용하여 스테이지별로 wav 파일화 시키기 위한 파이썬 코드
# edf + csv -> wav file
# signal_number 변수 설정 : 신호의 이름 설정
# 30초 단위로 wav 파일 생성

import pyedflib
import numpy as np
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
from scipy.io import wavfile
import csv

# 해당 경로상에 있는 edf 파일을 읽어들임
f = pyedflib.EdfReader("../edf_file_rea/test.edf")
n = f.signals_in_file
# 읽어들인 edf파일의 신호 레이블들을 저장
signal_labels = f.getSignalLabels()
print(signal_labels)

signal_number = 5       # wav파일로 변환하기 위한 신호 이름에 해당하는 리스트 인덱스 설정
fields_num = 4          # 시간에 해당하는 리스트 인덱스 설정(30초)

sigbufs = np.zeros((n, f.getNSamples()[signal_number]))     # 신호의 크기만큼 리스트 초기화
# print(f.getNSamples()[1])
# print(sigbufs)
sample_rate = f.getSampleFrequencies()[signal_number]   # wav파일로 변환하기 위한 신호의 sample_rate를 변수에 저장
# print(sample_rate)
signal_bufs = f.readSignal(signal_number)   # wav파일로 변환하기 위한 신호를 변수에 저장
# print(signal_bufs)

bef_bf = 0      # wav파일로 만들기 위한 시작 지점 초기화
aft_bf = 0      # wav파일로 만들기 위한 끝 지점 초기화
path = "../wav_dataset/"        # wav파일이 저장될 폴더 경로 지정
# name = "sdb2_"
name_max_index = 4      # 저장될 wav파일의 number 크기 설정(ex:0001)
name_before_number = ""     # wav파일의 number에서 0의 갯수 저장(ex:000)
name_index = 1          # wav파일의 number를 저장(ex:1~9999)
name_str = ""           # wav파일의 sleep stage string을 저장(ex:RR,WW,S1,S2,S3,S4)

# wav 파일을 생성하기 위한 csv 파일을 읽어들임
with open('../edf_file/test.csv', 'r') as reader:
    # 읽어들인 csv 파일 정보를 reader에 저장 후 라인별 for 루프
    for line in reader:
        # 라인별 ','을 기준으로 분류(리스트 형식)
        fields = line.split(',')
        print(fields[fields_num])

        # csv 파일에서 시간에 해당하는 값이 '30' 인 경우
        if fields[fields_num] == '30\n':
            aft_bf += sample_rate * 30              # 생성할 wav 파일의 범위 설정 (wav 파일의 제일 마지막 부분 설정)
            signal = signal_bufs[bef_bf:aft_bf]     # 생성할 wav 파일의 범위 설정 (처음 부분부터 마지막 부분까지 범위 설정)
            bef_bf = aft_bf                         # 다음에 생성할 wav 파일의 범위 설정 (방금 생성한 wav 파일의 마지막 부분을 처음으로 설정)

            name_str = str(name_index)              # wav 파일 번호

            # 생성할 wav 파일 이름에 존재하는 0의 갯수 설정
            for i in np.arange(name_max_index - len(name_str)):
                name_before_number += "0"

            # wav 파일 생성
            write(path + name_before_number + name_str + '.wav', sample_rate, signal)
            name_index += 1
            name_before_number = ""


