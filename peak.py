import pandas as pd

def find_min_y(file_path):
    # 读取CSV文件
    df = pd.read_csv(file_path)
    df = df.sort_values(by=['x', 'y'])
    
    # 获取唯一的x值
    unique_x = sorted(df['x'].unique())
    
    result = []
    i = 0

    while i < len(unique_x):
        x = unique_x[i]

        # 判断是否有相邻的x值
        adjacent_x = [x]
        while i + 1 < len(unique_x) and unique_x[i + 1] == unique_x[i] + 1:
            adjacent_x.append(unique_x[i + 1])
            i += 1
        
        # 筛选相邻x对应的所有y值
        sub_df = df[df['x'].isin(adjacent_x)]
        min_y_row = sub_df[sub_df['y'] == sub_df['y'].min()].iloc[0]
        
        result.append((int(min_y_row['x']), int(min_y_row['y'])))
        i += 1

    # 将结果保存到peak.csv
    result_df = pd.DataFrame(result, columns=['x', 'y'])
    result_df.to_csv('peak.csv', index=False)

    print(result)
    return result

# 使用示例
find_min_y('output.csv')
