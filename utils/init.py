import os
import shutil

def delete_all_files_in_folders(folders):
    """
    删除多个文件夹下的所有文件。

    :param folders: 包含多个文件夹路径的列表
    """
    for folder_path in folders:
        # 确保目标路径存在
        if not os.path.exists(folder_path):
            print(f"文件夹 {folder_path} 不存在！")
            continue

        # 遍历文件夹，删除所有文件
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            if os.path.isfile(file_path):
                os.remove(file_path)  # 删除文件
                # print(f"已删除文件：{file_path}")
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)  # 删除子文件夹及其内容
                # print(f"已删除文件夹及其内容：{file_path}")

# if __name__ == "__main__":
#     # 直接定义需要清空的文件夹路径列表
#     folder_paths = [
#         '/path/to/folder1',
#         '/path/to/folder2',
#         '/path/to/folder3'
#     ]
    
#     delete_all_files_in_folders(folder_paths)
