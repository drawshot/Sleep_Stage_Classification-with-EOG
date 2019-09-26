# 하나의 txt 파일을 csv 파일로 변환하기 위한 파이썬 코드

import csv

# 읽어들일 파일의 이름을 name 변수에 저장
name = 'ins2'

# name 변수에 저장된 이름을 이용해 txt 파일을 읽어들임
with open('data/' + name + '.txt', 'r') as in_file:
    # 읽어들인 txt 파일을 한줄 단위로 분리(리스트 형식)
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)

    # 같은 이름을 가지는 csv 파일 생성 및 저장
    with open('csv_data/'+name + '.csv', 'w') as out_file:
        writer = csv.writer(out_file)

        # txt 파일에서 읽어들인 리스트 내용들을 csv 파일에 저장
        writer.writerows(lines)