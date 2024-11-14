# 데이터 시각화 툴 

## 개요 
- 2차원 그래프 생성: 주어진 데이터에 대해 산점도(Scatter plot)와 선 그래프(Line plot)를 생성할 수 있습니다. 이 그래프는 데이터 간의 관계를 시각적으로 나타냅니다.
  
- 가로 방향 표: 실험 데이터가 가로 방향으로 배열된 표 형태로 시각화할 수 있습니다. 이 표는 주로 시간이나 단계별 데이터를 표시할 때 유용합니다.

- 세로 방향 표: 실험 데이터를 세로 방향으로 배열하여, 각 항목에 대한 세부 정보를 쉽게 비교할 수 있는 표를 생성할 수 있습니다.

## graph_visualization.py
데이터를 입력하여 2차원 그래프 변환 

![image](https://github.com/user-attachments/assets/6bfa75c1-defd-4e22-94c1-d2d708a86168)


## horizontal_table.py
데이터를 가로 방향 표 변환 

![image](https://github.com/user-attachments/assets/5313f0d0-8b3a-49f5-aee2-1b06cd3045fe)


## vertical_table.py
데이터를 세로 방향 표 변환 

![image](https://github.com/user-attachments/assets/89760f60-19e0-49d3-8d37-3ff013ccf99b)




# 사용 방법

***구글 코랩(추천)*** : 기본적으로 matplotlib 라이브러리가 존재하여 별다른 구축없이 실행 가능 

***vs code Ide*** : ```pip install matplotlib``` 라이브러리 설치 후 실행 

```
x_label = [1, 3, 5, 6, 8, 9]
y_label = [60, 68, 80, 47, 20, 30]

```
**공통** :  x축 ,y축 원하는 데이터 값 이름의 변수 사용 후 데이터 값 입력 

## graph-visualization.py
  
**b. 산점도 (Scatter plot)**
- plt.scatter(x_label, y_label, color='blue'): x_label과 y_label 데이터를 이용해 파란색 산점도를 생성합니다. 이 점들은 데이터를 시각적으로 나타내는 역할을 합니다.

**c. 선 그래프 (Line plot)**
- plt.plot(x_label, y_label, color='blue', linestyle='-', label='Trend Line'): x_label과 y_label을 기반으로 파란색 실선으로 연결된 선 그래프를 그립니다. label='Trend Line'은 범례에 표시될 이름을 설정합니다.

**d. 그래프 제목 설정**
- plt.title("temp - 880 °C"): 그래프 상단에 제목을 설정합니다. 여기서는 "temp - 880 °C"라는 제목을 설정했습니다.

**e. x축, y축 라벨 설정**
- plt.xlabel("hour"): x축의 라벨을 "hour"로 설정합니다.
- plt.ylabel("Strength"): y축의 라벨을 "Strength"로 설정합니다.

**f. 축 눈금 설정**
- plt.xticks(x_label): x축의 눈금을 x_label 데이터에 맞게 설정합니다.
- plt.yticks(y_label): y축의 눈금을 y_label 데이터에 맞게 설정합니다.

**g. 그리드 표시**
- plt.grid(): 그래프에 그리드를 추가하여 데이터의 비교가 용이하도록 합니다.

**h. 그래프 표시**
- plt.show(): 설정한 그래프를 화면에 출력합니다.


## horizontal-table.py

**a. Figure 생성 및 크기 조정**
- fig = plt.figure(figsize=(5, 1)): figsize를 사용하여 출력되는 그래프의 크기를 설정합니다. figsize=(5, 1)은 가로가 5, 세로가 1인 크기로 설정합니다. 이 값을 수정하여 표의 크기를 키울 수 있습니다.
b. 표 데이터
- table_data = [x_label, y_label]: 표에 표시할 데이터를 설정합니다. x_label은 x축 데이터(시간 등), y_label은 y축 데이터(강도 등)입니다.

**c. 표 추가 및 위치 조정**
- table = plt.table(cellText=table_data, rowLabels=['x_label', 'y_label'], cellLoc='center', loc='center'): plt.table을 사용하여 표를 생성합니다.
- cellText=table_data: 표에 들어갈 데이터.
- rowLabels=['x_label', 'y_label']: 표의 행 레이블을 설정합니다.
- cellLoc='center': 셀 내의 텍스트 정렬을 중앙으로 설정합니다.
- loc='center': 표의 위치를 화면 중앙으로 설정합니다.

**d. 표 글꼴 크기 및 스케일 조정**
- table.auto_set_font_size(False): 자동 글꼴 크기 조정을 비활성화합니다.
- table.set_fontsize(12): 글꼴 크기를 12로 설정합니다. 글꼴 크기를 조정하여 표의 가독성을 높일 수 있습니다.
- table.scale(1.1, 1.2): 표의 크기를 조정합니다. x축(가로) 비율을 1.1배, y축(세로) 비율을 1.2배로 설정하여 표의 크기를 약간 키울 수 있습니다.

**e. 불필요한 축 제거**
- plt.axis("off"): 불필요한 축을 제거하여 표만 출력되도록 설정합니다.

**f. 그래프 표시**
- plt.show(): 설정한 표를 화면에 출력합니다.

## vertical-table.py

**a. Figure 생성 및 크기 조정**
- fig = plt.figure(figsize=(6, 3)): figsize=(6, 3)을 사용하여 그래프의 크기를 설정합니다. 여기서 가로 크기를 6, 세로 크기를 3으로 설정하여 표가 화면에 더 잘 맞게 합니다. 필요에 따라 이 값을 조정할 수 있습니다.

**b. 데이터 준비**
- data = {'x_label': x_label, 'y_label': y_label}: x_label과 y_label 데이터를 딕셔너리로 변환합니다. 이때, 키는 x_label, y_label이고, 값은 각각 실험 데이터입니다.
- table_data = [list(data.keys())] + list(zip(*data.values())): 데이터를 표 형식에 맞게 변환합니다.
- data.keys()는 열 제목(x_label, y_label)을 반환하고,
- zip(*data.values())는 x_label과 y_label 데이터를 열로 변환하여 행렬 형식으로 만듭니다.

**c. 표 추가 및 위치 조정**
- table = plt.table(cellText=table_data, cellLoc='center', loc='center'): plt.table을 사용하여 표를 생성합니다.
- cellText=table_data: 데이터가 포함된 table_data를 표에 전달합니다.
- cellLoc='center': 셀 내의 텍스트 정렬을 중앙으로 설정합니다.
- loc='center': 표의 위치를 화면 중앙으로 설정하여 표가 균형 잡히게 보이도록 합니다.

**d. 표 글꼴 크기 및 스케일 조정**
- table.auto_set_font_size(False): 자동 글꼴 크기 조정을 비활성화하여, 수동으로 글꼴 크기를 조정할 수 있도록 합니다.
- table.set_fontsize(12): 글꼴 크기를 12로 설정하여 표의 텍스트가 너무 크거나 작지 않도록 적당히 조정합니다.
- table.scale(1.1, 1.5): 표의 크기를 x축(가로) 1.1배, y축(세로) 1.5배로 조정하여 표가 너무 작지 않도록 크기를 늘립니다.

**e. 불필요한 축 제거**
- plt.axis("off"): 불필요한 축을 제거하여 표만 표시되도록 합니다. 축이 없으면 표에 집중할 수 있습니다.

**f. 그래프 표시**
- plt.show(): 설정한 표를 화면에 표시합니다.





