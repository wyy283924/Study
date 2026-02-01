# Excel表合并工具 - 简化版
# 将员工基本信息表与员工绩效表合并

import pandas as pd
import os

def merge_excel_tables():
    """
    合并两个Excel表
    """
    print("Excel表合并工具")
    print("=" * 50)
    
    # 文件路径
    basic_file = "员工基本信息表.xlsx"
    performance_file = "员工绩效表.xlsx"
    
    # 检查文件是否存在
    if not os.path.exists(basic_file):
        print(f"错误：找不到 {basic_file}")
        return
    
    if not os.path.exists(performance_file):
        print(f"错误：找不到 {performance_file}")
        return
    
    try:
        # 读取基本信息表
        print(f"\n1. 读取基本信息表...")
        basic_df = pd.read_excel(basic_file)
        print(f"   形状：{basic_df.shape}")
        print(f"   列名：{list(basic_df.columns)}")
        
        # 读取绩效表
        print(f"\n2. 读取绩效表...")
        performance_df = pd.read_excel(performance_file)
        print(f"   形状：{performance_df.shape}")
        print(f"   列名：{list(performance_df.columns)}")
        
        # 查找共同字段
        basic_cols = set(basic_df.columns)
        performance_cols = set(performance_df.columns)
        common_cols = basic_cols & performance_cols
        
        print(f"\n3. 共同字段：{list(common_cols)}")
        
        # 选择关联键（通常选择第一个共同字段）
        if common_cols:
            join_key = list(common_cols)[0]
            print(f"   使用关联键：{join_key}")
        else:
            print("   错误：没有找到共同字段")
            return
        
        # 合并表
        print(f"\n4. 合并表...")
        merged_df = pd.merge(
            basic_df, 
            performance_df, 
            on=join_key, 
            how='left',
            suffixes=('_基本信息', '_绩效')
        )
        
        print(f"   合并后形状：{merged_df.shape}")
        print(f"   合并后列名：{list(merged_df.columns)}")
        
        # 保存结果
        output_file = "员工信息与绩效合并表.xlsx"
        print(f"\n5. 保存到 {output_file}...")
        
        with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
            # 保存合并数据
            merged_df.to_excel(writer, sheet_name='合并数据', index=False)
            
            # 保存数据概览
            overview = {
                '项目': ['总记录数', '基本信息字段数', '绩效字段数', '合并后字段数'],
                '数值': [
                    len(merged_df),
                    len([col for col in merged_df.columns if not col.endswith('_绩效')]),
                    len([col for col in merged_df.columns if col.endswith('_绩效')]),
                    len(merged_df.columns)
                ]
            }
            pd.DataFrame(overview).to_excel(writer, sheet_name='数据概览', index=False)
        
        print(f"   保存成功！")
        print(f"\n6. 合并结果预览：")
        print(merged_df.head())
        
        return merged_df
        
    except Exception as e:
        print(f"错误：{e}")
        return None

if __name__ == "__main__":
    merge_excel_tables()
