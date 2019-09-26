# 경로상에 존재하는 모든 txt파일을 csv파일로 변환하기 위한 파이썬 코드

import csv
import os

text_file = []

# 텍스트 파일 경로 설정('./edf_file/' 경로)
text_file = os.listdir('./edf_file/')

# 경로내의 모든 파일 수만큼 for 루프
for i in range(len(text_file)) :
    # '.'을 기준 리스트로 분리
    text_file_s = text_file[i].split('.')
    # 확장자가 'txt'인 경우 파일 이름을 변수에 저장
    if text_file_s[1] == 'txt' :
        name = text_file_s[0]
        # 변수에 저장된 txt 파일 이름을 이용해 txt 파일을 읽어들임
        with open('./edf_file/' + name + '.txt', 'r') as in_file :
            # 읽어들인 txt 파일을 한줄 단위로 분리(리스트 형식)
            stripped = (line.strip() for line in in_file)

            lines = (line.split(',') for line in stripped if line)

            # 변수에 저장된 같은 이름으로 csv 파일로 쓰기
            with open('./edf_file/' + name + '.csv', 'w') as out_file:
                writer = csv.writer(out_file)
                # txt 파일에서 읽어들인 한줄 단위별로 csv 파일에 저장
                writer.writerows(lines)
