import pandas as pd
import os

# 文件路径
basic_info_file = "员工基本信息表.xlsx"
performance_file = "员工绩效表.xlsx"

print("Excel文件字段分析")
print("=" * 50)

# 检查文件是否存在
if not os.path.exists(basic_info_file):
    print(f"错误：找不到文件 {basic_info_file}")
    exit()

if not os.path.exists(performance_file):
    print(f"错误：找不到文件 {performance_file}")
    exit()

try:
    # 读取员工基本信息表
    print(f"\n1. 读取文件：{basic_info_file}")
    print("-" * 30)
    basic_info_df = pd.read_excel(basic_info_file)
    
    print(f"数据形状：{basic_info_df.shape}")
    print(f"列名：{list(basic_info_df.columns)}")
    print(f"\n前3行数据：")
    print(basic_info_df.head(3))
    
    # 读取员工绩效表
    print(f"\n2. 读取文件：{performance_file}")
    print("-" * 30)
    performance_df = pd.read_excel(performance_file)
    
    print(f"数据形状：{performance_df.shape}")
    print(f"列名：{list(performance_df.columns)}")
    print(f"\n前3行数据：")
    print(performance_df.head(3))
    
    # 分析两个表的共同字段
    print(f"\n3. 字段对比分析")
    print("-" * 30)
    basic_columns = set(basic_info_df.columns)
    performance_columns = set(performance_df.columns)
    
    common_columns = basic_columns.intersection(performance_columns)
    basic_only = basic_columns - performance_columns
    performance_only = performance_columns - basic_columns
    
    print(f"基本信息表字段数：{len(basic_columns)}")
    print(f"绩效表字段数：{len(performance_columns)}")
    print(f"共同字段数：{len(common_columns)}")
    
    if common_columns:
        print(f"\n共同字段：{list(common_columns)}")
    
    if basic_only:
        print(f"\n仅在基本信息表中的字段：{list(basic_only)}")
    
    if performance_only:
        print(f"\n仅在绩效表中的字段：{list(performance_only)}")

except Exception as e:
    print(f"读取文件时出错：{str(e)}")
    print("请确保已安装pandas和openpyxl库：")
    print("pip install pandas openpyxl")
