import pandas as pd
import os

def read_excel_files():
    """
    读取员工基本信息表和员工绩效表，并显示字段信息
    """
    # 文件路径
    basic_info_file = "员工基本信息表.xlsx"
    performance_file = "员工绩效表.xlsx"
    
    print("=" * 60)
    print("Excel文件字段分析")
    print("=" * 60)
    
    # 检查文件是否存在
    if not os.path.exists(basic_info_file):
        print(f"错误：找不到文件 {basic_info_file}")
        return
    
    if not os.path.exists(performance_file):
        print(f"错误：找不到文件 {performance_file}")
        return
    
    try:
        # 读取员工基本信息表
        print(f"\n1. 读取文件：{basic_info_file}")
        print("-" * 40)
        basic_info_df = pd.read_excel(basic_info_file)
        
        print(f"数据形状：{basic_info_df.shape}")
        print(f"列名：{list(basic_info_df.columns)}")
        print(f"数据类型：")
        print(basic_info_df.dtypes)
        print(f"\n前5行数据：")
        print(basic_info_df.head())
        
        # 读取员工绩效表
        print(f"\n2. 读取文件：{performance_file}")
        print("-" * 40)
        performance_df = pd.read_excel(performance_file)
        
        print(f"数据形状：{performance_df.shape}")
        print(f"列名：{list(performance_df.columns)}")
        print(f"数据类型：")
        print(performance_df.dtypes)
        print(f"\n前5行数据：")
        print(performance_df.head())
        
        # 分析两个表的共同字段
        print(f"\n3. 字段对比分析")
        print("-" * 40)
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
        
        # 检查是否有可以作为关联键的字段
        print(f"\n4. 可能的关联键分析")
        print("-" * 40)
        for col in common_columns:
            basic_unique = basic_info_df[col].nunique()
            performance_unique = performance_df[col].nunique()
            basic_total = len(basic_info_df)
            performance_total = len(performance_df)
            
            print(f"字段 '{col}':")
            print(f"  基本信息表：{basic_unique} 个唯一值 / {basic_total} 总记录")
            print(f"  绩效表：{performance_unique} 个唯一值 / {performance_total} 总记录")
            
            if basic_unique == basic_total and performance_unique == performance_total:
                print(f"  ✓ 可能作为主键（在两个表中都是唯一的）")
            elif basic_unique == basic_total or performance_unique == performance_total:
                print(f"  ⚠ 在其中一个表中唯一，可能适合作为关联键")
            else:
                print(f"  - 不是唯一字段")
            print()
        
    except Exception as e:
        print(f"读取文件时出错：{str(e)}")
        print("请确保已安装pandas和openpyxl库：")
        print("pip install pandas openpyxl")

if __name__ == "__main__":
    read_excel_files()
