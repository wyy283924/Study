# 高级Excel合并工具
# 专门处理2024年第4季度绩效数据合并

import pandas as pd
import os
import re
from datetime import datetime

def filter_q4_2024_data(df):
    """
    筛选2024年第4季度的数据
    """
    print("筛选2024年第4季度数据...")
    
    # 查找可能包含日期或季度的列
    date_cols = []
    quarter_cols = []
    
    for col in df.columns:
        col_str = str(col).lower()
        if any(keyword in col_str for keyword in ['日期', 'date', '时间', 'time', '年', 'year', '月', 'month']):
            date_cols.append(col)
        if any(keyword in col_str for keyword in ['季度', 'quarter', 'q4', '第4季度', '第四季度']):
            quarter_cols.append(col)
    
    print(f"找到日期相关列：{date_cols}")
    print(f"找到季度相关列：{quarter_cols}")
    
    # 如果找到季度列，尝试筛选Q4数据
    if quarter_cols:
        for col in quarter_cols:
            print(f"\n检查列 '{col}' 的值：")
            unique_vals = df[col].unique()
            print(f"唯一值：{list(unique_vals)}")
            
            # 尝试筛选包含Q4的数据
            q4_patterns = ['Q4', '第4季度', '4季度', '第四季度', '2024年第四季度', '2024Q4']
            q4_mask = df[col].astype(str).str.contains('|'.join(q4_patterns), case=False, na=False)
            
            if q4_mask.any():
                q4_df = df[q4_mask].copy()
                print(f"找到Q4数据：{len(q4_df)} 条记录")
                return q4_df
    
    # 如果没有找到季度列，检查是否有2024年的数据
    if date_cols:
        for col in date_cols:
            print(f"\n检查列 '{col}' 的2024年数据：")
            try:
                # 尝试转换为日期格式
                df[col] = pd.to_datetime(df[col], errors='coerce')
                df_2024 = df[df[col].dt.year == 2024]
                if len(df_2024) > 0:
                    print(f"找到2024年数据：{len(df_2024)} 条记录")
                    # 进一步筛选第4季度（10-12月）
                    q4_2024 = df_2024[df_2024[col].dt.month.isin([10, 11, 12])]
                    if len(q4_2024) > 0:
                        print(f"找到2024年第4季度数据：{len(q4_2024)} 条记录")
                        return q4_2024
                    else:
                        print("未找到2024年第4季度数据，使用全部2024年数据")
                        return df_2024
            except:
                print(f"无法解析列 '{col}' 为日期格式")
    
    print("未找到明确的季度信息，使用全部绩效数据")
    return df

def smart_merge_tables(basic_df, performance_df):
    """
    智能合并两个表
    """
    print("\n智能合并表...")
    
    # 查找最佳关联键
    basic_cols = set(basic_df.columns)
    performance_cols = set(performance_df.columns)
    common_cols = basic_cols & performance_cols
    
    print(f"共同字段：{list(common_cols)}")
    
    if not common_cols:
        print("错误：没有找到共同字段")
        return None
    
    # 选择最佳关联键
    best_key = None
    best_score = 0
    
    for col in common_cols:
        basic_unique = basic_df[col].nunique()
        performance_unique = performance_df[col].nunique()
        basic_total = len(basic_df)
        performance_total = len(performance_df)
        
        # 计算匹配度
        if basic_unique == basic_total and performance_unique == performance_total:
            score = 100  # 完美匹配
        elif basic_unique == basic_total or performance_unique == performance_total:
            score = 80   # 单表唯一
        else:
            # 计算重叠度
            basic_vals = set(basic_df[col].dropna())
            performance_vals = set(performance_df[col].dropna())
            overlap = len(basic_vals & performance_vals)
            total_unique = len(basic_vals | performance_vals)
            score = (overlap / total_unique * 100) if total_unique > 0 else 0
        
        print(f"字段 '{col}': 匹配度 {score:.1f}%")
        
        if score > best_score:
            best_score = score
            best_key = col
    
    print(f"选择关联键：'{best_key}' (匹配度: {best_score:.1f}%)")
    
    # 执行合并
    merged_df = pd.merge(
        basic_df, 
        performance_df, 
        on=best_key, 
        how='left',
        suffixes=('_基本信息', '_绩效')
    )
    
    print(f"合并结果：{merged_df.shape}")
    return merged_df

def main():
    """
    主函数
    """
    print("高级Excel合并工具")
    print("目标：合并员工基本信息与2024年第4季度绩效")
    print("=" * 60)
    
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
        print(f"\n1. 读取基本信息表...")
        basic_df = pd.read_excel(basic_file)
        print(f"   形状：{basic_df.shape}")
        print(f"   列名：{list(basic_df.columns)}")
        
        # 读取绩效表
        print(f"\n2. 读取绩效表...")
        performance_df = pd.read_excel(performance_file)
        print(f"   形状：{performance_df.shape}")
        print(f"   列名：{list(performance_df.columns)}")
        
        # 筛选2024年第4季度数据
        print(f"\n3. 筛选2024年第4季度绩效数据...")
        q4_performance_df = filter_q4_2024_data(performance_df)
        print(f"   筛选后形状：{q4_performance_df.shape}")
        
        # 智能合并
        print(f"\n4. 智能合并表...")
        merged_df = smart_merge_tables(basic_df, q4_performance_df)
        
        if merged_df is None:
            print("合并失败")
            return
        
        # 保存结果
        output_file = "员工信息与2024Q4绩效合并表.xlsx"
        print(f"\n5. 保存到 {output_file}...")
        
        with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
            # 保存合并数据
            merged_df.to_excel(writer, sheet_name='合并数据', index=False)
            
            # 保存数据概览
            overview = {
                '统计项目': [
                    '基本信息表记录数',
                    '绩效表总记录数',
                    '2024Q4绩效记录数',
                    '合并后记录数',
                    '成功匹配记录数',
                    '未匹配记录数'
                ],
                '数值': [
                    len(basic_df),
                    len(performance_df),
                    len(q4_performance_df),
                    len(merged_df),
                    merged_df.dropna(subset=[col for col in merged_df.columns if col.endswith('_绩效')]).shape[0],
                    merged_df[merged_df.isnull().any(axis=1)].shape[0]
                ]
            }
            pd.DataFrame(overview).to_excel(writer, sheet_name='数据概览', index=False)
            
            # 保存原始数据（用于对比）
            basic_df.to_excel(writer, sheet_name='基本信息表', index=False)
            performance_df.to_excel(writer, sheet_name='绩效表', index=False)
            q4_performance_df.to_excel(writer, sheet_name='2024Q4绩效', index=False)
        
        print(f"   保存成功！")
        print(f"\n6. 合并结果预览：")
        print(merged_df.head())
        
        print(f"\n✅ 合并完成！")
        print(f"📁 输出文件：{output_file}")
        print(f"📊 包含工作表：合并数据、数据概览、基本信息表、绩效表、2024Q4绩效")
        
    except Exception as e:
        print(f"错误：{e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
