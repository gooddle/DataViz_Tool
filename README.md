# 데이터 시각화 툴 

## 개요 
실험 데이터 경우에 따라 2차원 그래프 및 가로 방향 표 혹은 세로 방향 표 전환 

## graph-visualization.py
실험 데이터를 입력하여 2차원 그래프 변환 

![image](https://github.com/user-attachments/assets/3a13d9cb-f7d8-4f76-9f53-fc3953acb724)

## horizontal-table.py
실험 데이터를 가로 방향 표 변환 

![image](https://github.com/user-attachments/assets/8d5379bb-a481-4f4c-bdcc-c8078de2cbdb)

## vertical-table.py
실험 데이터를 세로 방향 표 변환 

![image](https://github.com/user-attachments/assets/4c9196d4-cc5d-4f47-9b04-deb939de2e25)



# 사용 방법

구글 코랩 : 기본적으로 matplotlib 라이브러리가 존재하여 별다른 구축없이 실행 가능 

vs code Ide : ```pip install matplotlib``` 라이브러리 설치 후 실행 

```
x_label = [1, 3, 5, 6, 8, 9]
y_label = [60, 68, 80, 47, 20, 30]

```
공통 : 원하는 데이터 값 이름의 변수 사용 후 데이터 값 입력 

## graph-visualization.py
그래프에 title 설정 후 xlable,ylable를 데이터에 맞게 설정 


## horizontal-table.py

fig 크기 조절 

table_data 사용하는 데이터에 알맞게 table_data 변경

table 위치 조절 

표 크기 및 스케일 조절 

## vertical-table.py

fig 크기 조절 

data 원하는 데이터로 변경 

table 위치 조절 

표 크기 밑 스케일 조절 





