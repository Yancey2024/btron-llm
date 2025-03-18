import pandas as pd

def sort_and_group_csv(input_file, output_file):
    # 读取CSV文件
    df = pd.read_csv(input_file)
    
    # 按照x列排序
    df_sorted = df.sort_values(by=['x', 'y'], ascending=[True, True])
    
    # 保存结果到新的CSV文件
    df_sorted.to_csv(output_file, index=False)
    print(f"已保存到 {output_file}")

# 使用示例
sort_and_group_csv('/private/workspace/cy/btron/coordinates.csv', '/private/workspace/cy/btron/output.csv')
