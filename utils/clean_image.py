import os
from PIL import Image

def delete_small_images(folder_path):
    # 检查路径是否存在
    if not os.path.isdir(folder_path):
        print(f"路径不存在: {folder_path}")
        return

    # 遍历文件夹下的所有文件
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # 判断是否为图片
        if not filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
            continue

        try:
            # 打开图片获取尺寸
            with Image.open(file_path) as img:
                width, height = img.size

            # 删除横边像素小于200的图片
            if width < 200:
                os.remove(file_path)
                print(f"已删除: {file_path} (宽度: {width}px)")
        except Exception as e:
            print(f"处理失败: {file_path}, 错误: {e}")

# 使用示例
# 替换为你的图片文件夹路径
# folder_path = '/path/to/your/folder'
# delete_small_images(folder_path)
