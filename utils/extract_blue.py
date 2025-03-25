import os
import cv2
import numpy as np
import csv

def extract_blue_pixels(image_path, output_csv_path):
    # 读取图像
    image = cv2.imread(image_path)
    if image is None:
        # print(f"无法读取图像: {image_path}")
        return

    height, width, _ = image.shape
    if height != 280 or width != 555:
        # print(f"图像尺寸不符: {image_path}")
        return

    blue_pixels = []

    # 遍历固定区域，查找蓝色像素
    for y in range(111):
        for x in range(321):
            b, g, r = image[y, x]
            if b == 255 and g == 0 and r == 0:
                blue_pixels.append((x, y))

    for y in range(91):
        for x in range(321, 555):
            b, g, r = image[y, x]
            if b == 255 and g == 0 and r == 0:
                blue_pixels.append((x, y))

    # 排序：先按x升序，再按y升序
    blue_pixels.sort(key=lambda p: (p[0], p[1]))

    # 保存结果到CSV
    with open(output_csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['x', 'y'])
        writer.writerows(blue_pixels)
    # print(f"已保存蓝色像素坐标到: {output_csv_path}")

def process_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.png'):
            image_path = os.path.join(input_folder, filename)
            output_csv_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_blue_pixels.csv")
            extract_blue_pixels(image_path, output_csv_path)

# 使用示例
# input_folder = '/path/to/input/folder'
# output_folder = '/path/to/output/folder'
# process_folder(input_folder, output_folder)