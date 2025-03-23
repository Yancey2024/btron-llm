import cv2
import numpy as np
import csv

output_csv='gray.csv'
image_path = 'output.png'
# 读取图像

img = cv2.imread(image_path)

# 转换为RGB格式
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 定义灰色的RGB值
target_color = np.array([192, 192, 192])

# 找到所有灰色像素的位置
red_pixels = np.where(np.all(img_rgb == target_color, axis=-1))

# 转换为坐标列表
coordinates = list(zip(red_pixels[1], red_pixels[0]))

print(f"找到 {len(coordinates)} 个灰色像素。")

# 保存到CSV
with open(output_csv, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['x', 'y'])
    csvwriter.writerows(coordinates)

print(f"坐标已保存到 {output_csv}")


