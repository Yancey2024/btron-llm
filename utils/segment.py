import cv2
import numpy as np
import os

def extract_rectangle(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 获取所有图片
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('png', 'jpg', 'jpeg'))]

    if not image_files:
        print("没有找到图片")
        return

    for file_name in image_files:
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, file_name)

        # 读取图像
        image = cv2.imread(input_path)
        if image is None:
            print(f"无法读取图像: {file_name}")
            continue

        # 转换为灰度图像
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # 提取#808080颜色的区域 (128,128,128)
        lower_bound = np.array([128, 128, 128])
        upper_bound = np.array([128, 128, 128])
        mask = cv2.inRange(image, lower_bound, upper_bound)

        # 寻找边缘和轮廓
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if len(contours) == 0:
            print(f"未找到符合条件的矩形框: {file_name}")
            continue

        # 选择最大轮廓作为边框
        contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(contour)

        # 缩小边界，去除#808080像素边框
        x += 1
        y += 1
        w -= 2
        h -= 2

        if w <= 0 or h <= 0:
            print(f"裁剪后无有效区域: {file_name}")
            continue

        # 裁剪矩形框内的区域
        cropped_image = image[y:y+h, x:x+w]

        # 保存结果
        cv2.imwrite(output_path, cropped_image)
        print(f"裁剪完成，结果保存至: {output_path}")

# 使用示例
# extract_rectangle('input_folder_path', 'output_folder_path')
