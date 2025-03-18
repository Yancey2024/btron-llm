import cv2
import numpy as np
import csv

# 加载图像
image = cv2.imread('/private/workspace/cy/btron/output.png')  # 替换为你图像的路径

# 获取图像的尺寸
height, width, _ = image.shape

# 存储符合条件的坐标
coordinates = []

# 遍历图像的每个像素
for y in range(min(111, height)):  # 限制y最大为111
    for x in range(min(321, width)):  # 限制x最大为321
        # 获取当前像素的颜色值
        b, g, r = image[y, x]
        
        # 检查是否是蓝色像素 #0000ff
        if b == 255 and g == 0 and r == 0:
            coordinates.append([x, y])

# 保存坐标到CSV文件
with open('/private/workspace/cy/btron/coordinates.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['x', 'y'])  # 写入列名
    writer.writerows(coordinates)

print(f"共找到 {len(coordinates)} 个符合条件的坐标，并已保存到coordinates.csv")
