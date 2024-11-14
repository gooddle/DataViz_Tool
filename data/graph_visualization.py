import matplotlib.pyplot as plt

x_label = [1,2,3,4,5]
y_label = [1,2,3,4,5]


#산점도 (Scatter plot) 그리기
# hour 값을 x축, strength 값을 y축으로 하는 파란색 점들을 표시
plt.scatter(x_label, y_label, color='blue')  # blue로 산점도를 그림

# 선 그래프 (Line plot) 그리기
# hour 값을 x축, strength 값을 y축으로 하는 파란색 선을 그림
# `label`은 범례에 표시될 이름으로, 나중에 범례를 추가할 때 사용됨
plt.plot(x_label, y_label, color='blue', linestyle='-', label='Trend Line')

# 제목 설정
plt.title(" temp - 880 °C")  # 그래프의 제목을 설정

# x축과 y축 라벨 설정
plt.xlabel("hour")  # x축 라벨을 'hour'로 설정
plt.ylabel("Strength")  # y축 라벨을 'Strength'로 설정

# y축 눈금 (ticks) 설정
plt.xticks(x_label) # x축 눈금을 hour 데이터에 맞게 설정
plt.yticks(y_label)  # y축 눈금 (ticks) 설정
  
# 그리드 표시
plt.grid()  # 그래프에 그리드를 추가

# 그래프 표시
plt.show()  # 설정한 그래프를 화면에 출력