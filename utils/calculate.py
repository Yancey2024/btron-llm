import pandas as pd
import numpy as np
import os
import json

label = ['Horizontal','Vertical']

def linear_to_actual_y(y_value):
    return round(80 - (y_value / 280) * 100, 2)

def linear_to_logarithmic_x(x_value):
    log_min, log_max = np.log10(30), np.log10(1000)
    linear_min, linear_max = 0, 555
    log_value = log_min + (x_value - linear_min) / (linear_max - linear_min) * (log_max - log_min)
    return round(10 ** log_value, 2)

def correspond(file_path):
    df = pd.read_csv(file_path)
    
    df['log_x'] = df['x'].apply(linear_to_logarithmic_x)
    df['actual_y'] = df['y'].apply(linear_to_actual_y)
    
    return df

def process_directory(directory_path, output_directory):
    # 创建 final_result 文件夹（如果不存在的话）
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    # 获取目录中所有的CSV文件，并按文件名排序
    csv_files = sorted([f for f in os.listdir(directory_path) if f.endswith('.csv')])
    
    result = {}
    # 按顺序处理每个文件
    for index, filename in enumerate(csv_files):
        file_path = os.path.join(directory_path, filename)
        # print(f"Processing file: {filename}")
        
        # 处理文件并获取结果
        result_df = correspond(file_path)
                
        
        # 生成新的文件路径，将结果保存到 final_result 文件夹
        output_file_path = os.path.join(output_directory, filename)
        result_df.to_csv(output_file_path, index=False)

        result[label[index]] = result_df.to_dict(orient='records')

    #return json.dumps(result, ensure_ascii=False,indent=2)
    return result
        # print(f"Saved processed file: {output_file_path}")

# 使用示例
# 设定输入文件夹路径和输出文件夹路径
# input_directory = '/path/to/your/csv/files'
# output_directory = '/path/to/your/csv/files/final_result'

# process_directory(input_directory, output_directory)
