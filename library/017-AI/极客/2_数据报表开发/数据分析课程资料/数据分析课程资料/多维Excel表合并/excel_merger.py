#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Excel表合并工具
将员工基本信息表与员工绩效表合并，在基本信息基础上增加2024年第4季度绩效评分
"""

import pandas as pd
import os
from datetime import datetime

def analyze_excel_structure():
    """
    分析两个Excel表的结构
    """
    print("🔍 分析Excel表结构...")
    print("=" * 60)
    
    try:
        # 读取员工基本信息表
        basic_info_df = pd.read_excel("员工基本信息表.xlsx")
        print(f"📊 员工基本信息表：")
        print(f"   形状：{basic_info_df.shape}")
        print(f"   列名：{list(basic_info_df.columns)}")
        print(f"   前3行数据：")
        print(basic_info_df.head(3))
        
        # 读取员工绩效表
        performance_df = pd.read_excel("员工绩效表.xlsx")
        print(f"\n📊 员工绩效表：")
        print(f"   形状：{performance_df.shape}")
        print(f"   列名：{list(performance_df.columns)}")
        print(f"   前3行数据：")
        print(performance_df.head(3))
        
        # 分析共同字段
        basic_columns = set(basic_info_df.columns)
        performance_columns = set(performance_df.columns)
        common_columns = basic_columns.intersection(performance_columns)
        
        print(f"\n🔍 字段分析：")
        print(f"   基本信息表字段：{list(basic_columns)}")
        print(f"   绩效表字段：{list(performance_columns)}")
        print(f"   共同字段：{list(common_columns)}")
        
        return basic_info_df, performance_df, common_columns
        
    except Exception as e:
        print(f"❌ 分析表结构时出错：{str(e)}")
        return None, None, None

def find_join_key(basic_df, performance_df, common_columns):
    """
    找到最适合的关联键
    """
    print(f"\n🔑 寻找关联键...")
    print("=" * 60)
    
    best_key = None
    best_score = 0
    
    for col in common_columns:
        basic_unique = basic_df[col].nunique()
        performance_unique = performance_df[col].nunique()
        basic_total = len(basic_df)
        performance_total = len(performance_df)
        
        print(f"字段 '{col}':")
        print(f"   基本信息表：{basic_unique} 个唯一值 / {basic_total} 总记录")
        print(f"   绩效表：{performance_unique} 个唯一值 / {performance_total} 总记录")
        
        # 计算匹配度分数
        if basic_unique == basic_total and performance_unique == performance_total:
            score = 100  # 完美匹配
            print(f"   ✅ 完美匹配，推荐作为关联键")
        elif basic_unique == basic_total or performance_unique == performance_total:
            score = 80   # 单表唯一
            print(f"   ⚠️  单表唯一，可能适合作为关联键")
        else:
            # 计算重叠度
            basic_values = set(basic_df[col].dropna())
            performance_values = set(performance_df[col].dropna())
            overlap = len(basic_values.intersection(performance_values))
            total_unique = len(basic_values.union(performance_values))
            score = (overlap / total_unique * 100) if total_unique > 0 else 0
            print(f"   📊 重叠度：{overlap}/{total_unique} ({score:.1f}%)")
        
        if score > best_score:
            best_score = score
            best_key = col
        
        print()
    
    print(f"🎯 推荐关联键：'{best_key}' (匹配度: {best_score:.1f}%)")
    return best_key

def merge_excel_tables(basic_df, performance_df, join_key):
    """
    合并两个Excel表
    """
    print(f"\n🔄 开始合并表...")
    print("=" * 60)
    
    try:
        # 检查关联键是否存在
        if join_key not in basic_df.columns or join_key not in performance_df.columns:
            print(f"❌ 关联键 '{join_key}' 不存在于两个表中")
            return None
        
        # 检查数据质量
        basic_missing = basic_df[join_key].isna().sum()
        performance_missing = performance_df[join_key].isna().sum()
        
        print(f"数据质量检查：")
        print(f"   基本信息表 '{join_key}' 缺失值：{basic_missing}")
        print(f"   绩效表 '{join_key}' 缺失值：{performance_missing}")
        
        # 清理数据 - 移除关联键的缺失值
        basic_clean = basic_df.dropna(subset=[join_key]).copy()
        performance_clean = performance_df.dropna(subset=[join_key]).copy()
        
        print(f"清理后数据：")
        print(f"   基本信息表：{len(basic_clean)} 行")
        print(f"   绩效表：{len(performance_clean)} 行")
        
        # 执行左连接（以基本信息表为主）
        merged_df = pd.merge(
            basic_clean, 
            performance_clean, 
            on=join_key, 
            how='left',
            suffixes=('_基本信息', '_绩效')
        )
        
        print(f"合并结果：")
        print(f"   合并后行数：{len(merged_df)}")
        print(f"   合并后列数：{len(merged_df.columns)}")
        
        # 检查匹配情况
        matched_count = merged_df.dropna(subset=[col for col in performance_clean.columns if col != join_key]).shape[0]
        print(f"   成功匹配的记录：{matched_count}")
        print(f"   未匹配的记录：{len(merged_df) - matched_count}")
        
        return merged_df
        
    except Exception as e:
        print(f"❌ 合并表时出错：{str(e)}")
        return None

def filter_2024_q4_performance(performance_df):
    """
    筛选2024年第4季度的绩效数据
    """
    print(f"\n📅 筛选2024年第4季度绩效数据...")
    print("=" * 60)
    
    # 查找可能包含日期或季度的列
    date_columns = []
    quarter_columns = []
    
    for col in performance_df.columns:
        col_lower = str(col).lower()
        if any(keyword in col_lower for keyword in ['日期', 'date', '时间', 'time', '年', 'year', '月', 'month']):
            date_columns.append(col)
        if any(keyword in col_lower for keyword in ['季度', 'quarter', 'q4', '第4季度']):
            quarter_columns.append(col)
    
    print(f"可能的日期列：{date_columns}")
    print(f"可能的季度列：{quarter_columns}")
    
    # 如果找到季度列，尝试筛选Q4数据
    if quarter_columns:
        for col in quarter_columns:
            print(f"\n检查列 '{col}' 的值：")
            unique_values = performance_df[col].unique()
            print(f"   唯一值：{list(unique_values)}")
            
            # 尝试筛选包含Q4或第4季度的数据
            q4_mask = performance_df[col].astype(str).str.contains('Q4|第4季度|4季度|第四季度', case=False, na=False)
            if q4_mask.any():
                q4_df = performance_df[q4_mask].copy()
                print(f"   找到Q4数据：{len(q4_df)} 条记录")
                return q4_df
    
    # 如果没有找到季度列，返回原始数据
    print("   未找到明确的季度信息，使用全部绩效数据")
    return performance_df

def save_merged_excel(merged_df, output_filename="员工信息与绩效合并表.xlsx"):
    """
    保存合并后的Excel文件
    """
    print(f"\n💾 保存合并结果...")
    print("=" * 60)
    
    try:
        # 创建Excel写入器
        with pd.ExcelWriter(output_filename, engine='openpyxl') as writer:
            # 保存合并后的数据
            merged_df.to_excel(writer, sheet_name='合并数据', index=False)
            
            # 添加数据概览表
            overview_data = {
                '统计项目': [
                    '总记录数',
                    '基本信息字段数',
                    '绩效字段数',
                    '合并后字段数',
                    '成功匹配记录数',
                    '未匹配记录数'
                ],
                '数值': [
                    len(merged_df),
                    len([col for col in merged_df.columns if col.endswith('_基本信息') or not col.endswith('_绩效')]),
                    len([col for col in merged_df.columns if col.endswith('_绩效')]),
                    len(merged_df.columns),
                    merged_df.dropna(subset=[col for col in merged_df.columns if col.endswith('_绩效')]).shape[0],
                    merged_df[merged_df.isnull().any(axis=1)].shape[0]
                ]
            }
            
            overview_df = pd.DataFrame(overview_data)
            overview_df.to_excel(writer, sheet_name='数据概览', index=False)
        
        print(f"✅ 合并结果已保存到：{output_filename}")
        print(f"📊 文件包含两个工作表：")
        print(f"   - 合并数据：包含所有合并后的数据")
        print(f"   - 数据概览：包含统计信息")
        
        return True
        
    except Exception as e:
        print(f"❌ 保存文件时出错：{str(e)}")
        return False

def main():
    """
    主函数
    """
    print("🚀 Excel表合并工具启动")
    print("=" * 80)
    print("目标：将员工基本信息表与2024年第4季度绩效评分合并")
    print("=" * 80)
    
    # 检查文件是否存在
    basic_file = "员工基本信息表.xlsx"
    performance_file = "员工绩效表.xlsx"
    
    if not os.path.exists(basic_file):
        print(f"❌ 错误：找不到文件 {basic_file}")
        return
    
    if not os.path.exists(performance_file):
        print(f"❌ 错误：找不到文件 {performance_file}")
        return
    
    # 步骤1：分析表结构
    basic_df, performance_df, common_columns = analyze_excel_structure()
    if basic_df is None:
        return
    
    # 步骤2：筛选2024年第4季度绩效数据
    performance_q4_df = filter_2024_q4_performance(performance_df)
    
    # 步骤3：找到关联键
    join_key = find_join_key(basic_df, performance_q4_df, common_columns)
    if not join_key:
        print("❌ 无法找到合适的关联键")
        return
    
    # 步骤4：合并表
    merged_df = merge_excel_tables(basic_df, performance_q4_df, join_key)
    if merged_df is None:
        return
    
    # 步骤5：保存结果
    success = save_merged_excel(merged_df)
    
    if success:
        print(f"\n🎉 合并完成！")
        print(f"📁 输出文件：员工信息与绩效合并表.xlsx")
        print(f"📊 合并后数据预览：")
        print(merged_df.head())
    else:
        print(f"\n💥 合并失败，请检查错误信息")

if __name__ == "__main__":
    main()
