# Excel文件字段分析 - 手动运行版本
# 请将此代码复制到您的Python环境中运行

import pandas as pd
import os

def main():
    print("Excel文件字段分析")
    print("=" * 50)
    
    # 文件路径
    basic_file = "员工基本信息表.xlsx"
    performance_file = "员工绩效表.xlsx"
    
    # 检查文件
    if not os.path.exists(basic_file):
        print(f"错误：找不到 {basic_file}")
        return
    
    if not os.path.exists(performance_file):
        print(f"错误：找不到 {performance_file}")
        return
    
    try:
        # 读取基本信息表
        print(f"\n1. 基本信息表：{basic_file}")
        print("-" * 30)
        df1 = pd.read_excel(basic_file)
        print(f"形状：{df1.shape}")
        print(f"列名：{list(df1.columns)}")
        print(f"前3行：")
        print(df1.head(3))
        
        # 读取绩效表
        print(f"\n2. 绩效表：{performance_file}")
        print("-" * 30)
        df2 = pd.read_excel(performance_file)
        print(f"形状：{df2.shape}")
        print(f"列名：{list(df2.columns)}")
        print(f"前3行：")
        print(df2.head(3))
        
        # 字段对比
        print(f"\n3. 字段对比")
        print("-" * 30)
        cols1 = set(df1.columns)
        cols2 = set(df2.columns)
        common = cols1 & cols2
        only1 = cols1 - cols2
        only2 = cols2 - cols1
        
        print(f"共同字段：{list(common)}")
        print(f"仅基本信息表：{list(only1)}")
        print(f"仅绩效表：{list(only2)}")
        
    except Exception as e:
        print(f"错误：{e}")

if __name__ == "__main__":
    main()
