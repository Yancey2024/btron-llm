import os
import re

def clean_name(filename):
    # 删除中文和空格
    filename = re.sub(r'[\u4e00-\u9fff]', '', filename)
    filename = filename.replace(" ", "")
    return filename

def rename_images(folder_path):
    if not os.path.isdir(folder_path):
        # print("指定的路径不是文件夹")
        return
    
    images = [f for f in os.listdir(folder_path) if f.lower().endswith(('jpg', 'jpeg', 'png', 'bmp'))]
    images.sort()  # 确保按顺序处理

    for i, filename in enumerate(images, start=1):
        name, ext = os.path.splitext(filename)
        new_name = f"report_{i}{ext}"
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        # print(f"重命名: {filename} -> {new_name}")

# 使用示例
# folder_path = "C:/your/folder/path"  # 替换为你的文件夹路径
# rename_images(folder_path)
