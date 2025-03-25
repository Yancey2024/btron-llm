import os
import pandas as pd

def process_csv(input_file: str, output_file: str):
    # 读取CSV文件
    df = pd.read_csv(input_file)

    # 第一步：对同一个x值，仅保留其中最小的y值
    df_min_y = df.loc[df.groupby('x')['y'].idxmin()]

    # 第二步：处理相邻的x值
    # 首先，按x升序排序
    df_min_y = df_min_y.sort_values(by='x')

    # 初始化处理后的结果
    result = []

    # 遍历DataFrame中的每一行，检查相邻的x值
    i = 0
    while i < len(df_min_y):
        # 找到当前x值和y值
        current_x = df_min_y.iloc[i]['x']
        current_y = df_min_y.iloc[i]['y']
        
        # 记录当前x值和y值（即最小y值对应的x）
        min_x = current_x
        min_y = current_y

        # 如果下一个x值与当前x值相邻，进行合并
        j = i + 1
        while j < len(df_min_y) and df_min_y.iloc[j]['x'] == current_x + 1:
            # 选择最小的y值
            if df_min_y.iloc[j]['y'] < min_y:
                min_y = df_min_y.iloc[j]['y']
                min_x = current_x + 1  # 保持当前相邻x值的关系
            current_x = df_min_y.iloc[j]['x']
            j += 1

        # 将合并后的最小y值和对应的x值添加到结果中
        result.append((min_x, min_y))

        # 跳到下一个不相邻的x值
        i = j

    # 将结果转换为DataFrame
    result_df = pd.DataFrame(result, columns=['x', 'y'])

    # 保存结果到新的CSV文件
    result_df.to_csv(output_file, index=False)

    return result_df

def process_multiple_csv_files(input_folder: str, output_folder: str):
    # 获取文件夹中所有CSV文件
    for filename in os.listdir(input_folder):
        if filename.endswith('.csv'):
            input_file = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, f"processed_{filename}")
            # print(f"Processing file: {filename}")
            process_csv(input_file, output_file)

# 调用函数处理文件夹中的所有CSV文件
# input_folder = 'your_input_folder'  # 输入文件夹路径
# output_folder = 'your_output_folder'  # 输出文件夹路径
# process_multiple_csv_files(input_folder, output_folder)
