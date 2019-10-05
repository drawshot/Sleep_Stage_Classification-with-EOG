## Sleep Stage Classification with EOG
EOG 신호를 이용한 머신러닝 기반의 수면 단계 분류

### 프로젝트 기간
2018-08-01 ~ 2019-04-30

### 프로젝트 설명
수면은 인간의 일상에 많은 비중을 차지하고 있다. 수면은 무의식 상태를 유지하며, 신체 및 정신에 휴식을 제공하여 건강을 회복, 유지 시켜주는 과정을 말한다.
수면은 크게 렘수면(rapid eye movement : REM), 비렘수면(non-rapid eye movement : non-REM)으로 구분할 수 있으며, 비렘수면은 수면의 깊이에 따라서 다시 S1(1단계), S2(2단계), S3(3단계), S4(4단계)로 구분할 수 있다.
프로젝트의 목표는 흔히 EEG, EMG 채널을 이용한 수면 단계 분류가 아닌 안전위도(electrooculogram : EOG) 신호를 이용해 수면 단계를 분류하여 수면다원검사를 대체할 수 있는 머신러닝 알고리즘 개발을 목표로 한다.
수면 단계를 분류하기 위하여 합성곱 신경망(Convolution Neural Networks : CNN) 알고리즘을 이용하여 학습 및 테스트를 하였으며, 이에 사용된 모델은 Inception-v3 모델을 사용하였다.
<br />
<br />
수면 단계 분류 알고리즘의 전체적인 흐름
* EDF 데이터를 EEG, EOG, EMG 채널별로 분리(wav 파일로 저장)
* 판독 주기에 따라 30초 단위의 윈도우로 분리
* 분리된 데이터를 스펙트로그램 이미지로 변환 후 저장
* Inception-v3 모델을 이용하여 학습 및 테스트
<img width="237" alt="스크린샷 2019-09-26 오후 3 23 23" src="https://user-images.githubusercontent.com/26424846/65943912-870e3680-e46b-11e9-9808-5c0df504030e.png">

```python

```
