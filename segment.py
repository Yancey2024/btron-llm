import cv2
import numpy as np

# 图片路径配置
input_path = '/private/workspace/cy/btron/input.png'
output_path = '/private/workspace/cy/btron/output.png'

def extract_rectangle(input_path, output_path):
    # 读取图像
    image = cv2.imread(input_path)
    if image is None:
        print("无法读取图像")
        return

    # 转换为灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 提取#808080颜色的区域 (128,128,128)
    lower_bound = np.array([128, 128, 128])
    upper_bound = np.array([128, 128, 128])
    mask = cv2.inRange(image, lower_bound, upper_bound)

    # 寻找边缘和轮廓
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) == 0:
        print("未找到符合条件的矩形框")
        return

    # 选择最大轮廓作为边框
    contour = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(contour)

    # 缩小边界，去除#808080像素边框
    x += 1
    y += 1
    w -= 2
    h -= 2

    if w <= 0 or h <= 0:
        print("裁剪后无有效区域")
        return

    # 裁剪矩形框内的区域
    cropped_image = image[y:y+h, x:x+w]

    # 保存结果
    cv2.imwrite(output_path, cropped_image)
    print(f"裁剪完成，结果保存至: {output_path}")

# 使用示例
extract_rectangle(input_path, output_path)