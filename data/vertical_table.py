import matplotlib.pyplot as plt


x_label = [1,2,3,4,5]
y_label = [1,2,3,4,5]

# Figure 생성 (size 조정)
fig = plt.figure(figsize=(6, 3))  # 크기를 약간 줄임

# 데이터를 표로 표시
data = {'x_label': x_label, 'y_label': y_label}
table_data = [list(data.keys())] + list(zip(*data.values()))

# 표를 추가하고 위치 조정
table = plt.table(cellText=table_data, cellLoc='center', loc='center')

# 표 글꼴 크기 및 스케일 조정
table.auto_set_font_size(False)
table.set_fontsize(12)  # 글꼴 크기 적당히 설정
table.scale(1.1, 1.5)    # 표 크기를 약간만 키움

# 불필요한 축 제거
plt.axis("off")

# 그래프 표시
plt.show()