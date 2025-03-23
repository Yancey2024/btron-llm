import pandas as pd
import numpy as np

def linear_to_actual_y(y_value):
    return 80 - (y_value / 280) * 100

def linear_to_logarithmic_x(x_value):
    log_min, log_max = np.log10(30), np.log10(1000)
    linear_min, linear_max = 0, 555
    log_value = log_min + (x_value - linear_min) / (linear_max - linear_min) * (log_max - log_min)
    return 10 ** log_value

def process_csv(file_path):
    df = pd.read_csv(file_path)
    
    df['log_x'] = df['x'].apply(linear_to_logarithmic_x)
    df['actual_y'] = df['y'].apply(linear_to_actual_y)
    
    print(df)
    return df

# 使用示例
process_csv('peak.csv')
