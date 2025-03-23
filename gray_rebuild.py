import numpy as np
import cv2
import pandas as pd

def create_png_from_csv(csv_path, output_path='output_rebuild.png', width=555, height=280):
    # 创建一个全白的图像 (255表示白色)
    image = np.ones((height, width), dtype=np.uint8) * 255

    # 读取CSV文件
    df = pd.read_csv(csv_path)

    # 遍历CSV数据，将指定坐标的像素标为黑色
    for _, row in df.iterrows():
        x, y = int(row['x']), int(row['y'])
        if 0 <= x < width and 0 <= y < height:
            image[y, x] = 0
        else:
            print(f"警告：坐标 ({x}, {y}) 超出范围，已跳过。")

    # 保存PNG图像
    cv2.imwrite(output_path, image)
    print(f"图像已保存至 {output_path}")

# 使用示例
create_png_from_csv('gray_output.csv')
