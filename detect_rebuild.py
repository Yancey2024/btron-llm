import numpy as np
import cv2

def get_border_black_pixels(image_path, width=555, height=280):
    # 读取PNG图像
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("无法读取图像")
        return []

    border_black_pixels = []

    # 上边界和下边界
    for x in range(width):
        if image[0, x] == 0:
            border_black_pixels.append((x, 0))
        if image[height-1, x] == 0:
            border_black_pixels.append((x, height-1))

    # 左边界和右边界
    for y in range(height):
        if image[y, 0] == 0:
            border_black_pixels.append((0, y))
        if image[y, width-1] == 0:
            border_black_pixels.append((width-1, y))

    # 排序
    border_black_pixels.sort(key=lambda p: (p[1] != 0, p[0] if p[1] == 0 else 0, p[0] == 0, p[1] if p[0] == 0 else 0))

    print("外围黑色像素坐标：", border_black_pixels)
    return border_black_pixels

# 使用示例
get_border_black_pixels('output_rebuild.png')
