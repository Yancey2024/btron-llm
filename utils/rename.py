import os
import re

def remove_spaces(text):
    # 删除文件名中的空格
    return text.replace(" ", "")

def rename_images(folder_path):
    if not os.path.isdir(folder_path):
        print("指定的路径不是文件夹")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path) and filename.lower().endswith(('jpg', 'jpeg', 'png', 'bmp')):
            name, ext = os.path.splitext(filename)
            name_no_spaces = remove_spaces(name)
            new_name = "report" + ext

            new_file_path = os.path.join(folder_path, new_name)

            # 检查重名，避免覆盖
            counter = 1
            while os.path.exists(new_file_path):
                new_name = f"report_{counter}{ext}"
                new_file_path = os.path.join(folder_path, new_name)
                counter += 1

            os.rename(file_path, new_file_path)
            print(f"重命名: {filename} -> {new_name}")

# if __name__ == "__main__":
#     # 直接在此处定义文件夹路径
#     folder_path = "C:/your/folder/path"  # 替换成你的文件夹路径
#     rename_images(folder_path)
