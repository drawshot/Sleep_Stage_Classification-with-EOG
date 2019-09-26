# 경로상에 존재하는 S3 스테이지의 wav 파일을 모두 스펙트로그램 이미지로 변환
# after_path 리스트 변수 설정 : 스펙트로그램 이미지의 저장 경로 설정

import pyedflib
import numpy as np
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
from scipy.io import wavfile
import os


before_wav_file_path = "test_dataset/sdb2_"
after_wav_file_path = ""

before_postprocessing_image_path = "test_image_set/sdb2_"
after_postprocessing_image_path = ""

before_path = ['RR_dataset/', 'S1_dataset/', 'S2_dataset/', 'S3_dataset/', 'S4_dataset/', 'WW_dataset/']
after_path = ['image_RR_dataset/', 'image_S1_dataset/', 'image_S2_dataset/', 'image_S3_dataset/', 'image_S4_dataset/', 'image_WW_dataset/']


# wav_file = ['wav_file_RR', 'wav_file_S1', 'wav_file_S2', 'wav_file_S3', 'wav_file_S4', 'wav_file_S5']
# wav_file_RR = os.listdir('./RR_dataset/')
# wav_file_S1 = os.listdir('./S1_dataset/')
# wav_file_S2 = os.listdir('./S2_dataset/')
# wav_file_S3 = os.listdir('./S3_dataset/')
# wav_file_S4 = os.listdir('./S4_dataset/')
# wav_file_WW = os.listdir('./WW_dataset/')

wav_file_stage = [[],[],[],[],[],[]]
wav_file_stage[0] = os.listdir('./RR_dataset/')
wav_file_stage[1] = os.listdir('./S1_dataset/')
wav_file_stage[2] = os.listdir('./S2_dataset/')
wav_file_stage[3] = os.listdir('./S3_dataset/')
wav_file_stage[4] = os.listdir('./S4_dataset/')
wav_file_stage[5] = os.listdir('./WW_dataset/')

# print(wav_file_stage[1])
# print(wav_file_RR[0].split('.')[0])

# for number in range(6):
number = 3
for i in range(len(wav_file_stage[number])):
    sample_frequency, signalData = wavfile.read(before_path[number] + wav_file_stage[number][i])
    Pxx, freqs, bins, im = plt.specgram(signalData[:], Fs=sample_frequency)
    plt.savefig(after_path[number] + wav_file_stage[number][i].split('.')[0] + ".jpg")


# for i in range(len(wav_file_RR)) :
#     sample_frequency, signalData = wavfile.read(before_path[0] + wav_file_RR[i])
#     Pxx, freqs, bins, im = plt.specgram(signalData[:], Fs=sample_frequency)
#     plt.savefig(after_path[0] + wav_file_RR[i].split('.')[0] + ".jpg")



## make image file
# for i in np.arange(1152):
#     name_len = len(str(i+file_num))
#     zero_len = 4 - name_len
#     # print(zero_len)
#
#     for a in np.arange(zero_len):
#         after_wav_file_path += "0"
#         after_postprocessing_image_path += "0"
#
#     after_wav_file_path += str(i+file_num)
#     after_postprocessing_image_path += str(i+file_num)
#
#     sample_frequency, signalData = wavfile.read(before_wav_file_path + after_wav_file_path + ".wav")
#     Pxx, freqs, bins, im = plt.specgram(signalData[:], Fs=sample_frequency)
#     plt.savefig(before_postprocessing_image_path + after_postprocessing_image_path + ".jpg")
#
#     after_wav_file_path = ""
#     after_postprocessing_image_path = ""

