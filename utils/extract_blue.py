import cv2
import numpy as np
import csv
import os

def process_images_in_folder(image_folder, output_folder, color_to_find=(255, 0, 0), 
                             min_x=0, max_x=321, min_y=0, max_y=111):
    """
    批量处理文件夹中的图像，并根据指定的颜色输出坐标到CSV文件。

    :param image_folder: 图像所在文件夹的路径
    :param output_folder: 输出CSV文件的文件夹路径
    :param color_to_find: 要查找的颜色，默认为蓝色 (255, 0, 0)（BGR格式）
    :param min_x: 最小x坐标限制，默认为0
    :param max_x: 最大x坐标限制，默认为321
    :param min_y: 最小y坐标限制，默认为0
    :param max_y: 最大y坐标限制，默认为111
    """
    # 创建输出文件夹（如果不存在）
    os.makedirs(output_folder, exist_ok=True)

    # 获取文件夹中所有图像文件
    image_files = [f for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

    # 批量处理每个图像
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        csv_path = os.path.join(output_folder, f"{os.path.splitext(image_file)[0]}_coordinates.csv")
        
        # 加载图像
        image = cv2.imread(image_path)
        if image is None:
            print(f"无法加载图像 {image_file}，跳过该文件。")
            continue

        # 获取图像的尺寸
        height, width, _ = image.shape

        # 存储符合条件的坐标
        coordinates = []

        # 遍历图像的每个像素
        for y in range(min(max_y, height)):  # 限制y最大为max_y
            for x in range(min(max_x, width)):  # 限制x最大为max_x
                # 忽略小于min_x和min_y的像素
                if x < min_x or y < min_y:
                    continue
                
                # 获取当前像素的颜色值
                b, g, r = image[y, x]
                
                # 检查是否是指定颜色像素
                if (b, g, r) == color_to_find:
                    coordinates.append([x, y])

        # 保存坐标到CSV文件
        with open(csv_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['x', 'y'])  # 写入列名
            writer.writerows(coordinates)

        print(f"图像 {image_file} 处理完成，找到 {len(coordinates)} 个符合条件的坐标，并已保存到 {csv_path}")

# 定义图像文件夹路径和输出文件夹路径
# image_folder = '/private/workspace/cy/btron/images'  # 图像文件夹路径
# output_folder = '/private/workspace/cy/btron/outputs'  # 输出CSV文件的文件夹路径

# 调用函数处理图像文件夹中的所有图像
# process_images_in_folder(image_folder, output_folder)

# 调用函数时使用最大和最小坐标限制
# process_images_in_folder("segmented_pics", "extracted_blue", min_x=0, max_x=321, min_y=0, max_y=111)
# process_images_in_folder("segmented_pics", "extracted_blue", min_x=322, max_x=555, min_y=0, max_y=91)
