#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Excel文件字段分析工具
用于分析员工基本信息表和员工绩效表的字段结构
"""

import pandas as pd
import os
import sys

def analyze_excel_files():
    """
    分析Excel文件的字段结构
    """
    # 文件路径
    basic_info_file = "员工基本信息表.xlsx"
    performance_file = "员工绩效表.xlsx"
    
    print("=" * 80)
    print("Excel文件字段分析工具")
    print("=" * 80)
    
    # 检查文件是否存在
    if not os.path.exists(basic_info_file):
        print(f"❌ 错误：找不到文件 {basic_info_file}")
        print("请确保文件在当前目录下")
        return False
    
    if not os.path.exists(performance_file):
        print(f"❌ 错误：找不到文件 {performance_file}")
        print("请确保文件在当前目录下")
        return False
    
    try:
        # 读取员工基本信息表
        print(f"\n📊 1. 分析文件：{basic_info_file}")
        print("=" * 60)
        basic_info_df = pd.read_excel(basic_info_file)
        
        print(f"📈 数据形状：{basic_info_df.shape[0]} 行 × {basic_info_df.shape[1]} 列")
        print(f"📋 列名：")
        for i, col in enumerate(basic_info_df.columns, 1):
            print(f"   {i:2d}. {col}")
        
        print(f"\n📝 数据类型：")
        for col, dtype in basic_info_df.dtypes.items():
            print(f"   {col}: {dtype}")
        
        print(f"\n👀 前3行数据预览：")
        print(basic_info_df.head(3).to_string())
        
        # 读取员工绩效表
        print(f"\n📊 2. 分析文件：{performance_file}")
        print("=" * 60)
        performance_df = pd.read_excel(performance_file)
        
        print(f"📈 数据形状：{performance_df.shape[0]} 行 × {performance_df.shape[1]} 列")
        print(f"📋 列名：")
        for i, col in enumerate(performance_df.columns, 1):
            print(f"   {i:2d}. {col}")
        
        print(f"\n📝 数据类型：")
        for col, dtype in performance_df.dtypes.items():
            print(f"   {col}: {dtype}")
        
        print(f"\n👀 前3行数据预览：")
        print(performance_df.head(3).to_string())
        
        # 分析两个表的共同字段
        print(f"\n🔍 3. 字段对比分析")
        print("=" * 60)
        basic_columns = set(basic_info_df.columns)
        performance_columns = set(performance_df.columns)
        
        common_columns = basic_columns.intersection(performance_columns)
        basic_only = basic_columns - performance_columns
        performance_only = performance_columns - basic_columns
        
        print(f"📊 统计信息：")
        print(f"   基本信息表字段数：{len(basic_columns)}")
        print(f"   绩效表字段数：{len(performance_columns)}")
        print(f"   共同字段数：{len(common_columns)}")
        
        if common_columns:
            print(f"\n🤝 共同字段：")
            for i, col in enumerate(sorted(common_columns), 1):
                print(f"   {i:2d}. {col}")
        
        if basic_only:
            print(f"\n📋 仅在基本信息表中的字段：")
            for i, col in enumerate(sorted(basic_only), 1):
                print(f"   {i:2d}. {col}")
        
        if performance_only:
            print(f"\n📊 仅在绩效表中的字段：")
            for i, col in enumerate(sorted(performance_only), 1):
                print(f"   {i:2d}. {col}")
        
        # 检查可能的关联键
        print(f"\n🔑 4. 关联键分析")
        print("=" * 60)
        print("分析哪些字段可能用作两个表的关联键：")
        
        for col in common_columns:
            basic_unique = basic_info_df[col].nunique()
            performance_unique = performance_df[col].nunique()
            basic_total = len(basic_info_df)
            performance_total = len(performance_df)
            
            print(f"\n字段 '{col}':")
            print(f"   基本信息表：{basic_unique} 个唯一值 / {basic_total} 总记录")
            print(f"   绩效表：{performance_unique} 个唯一值 / {performance_total} 总记录")
            
            if basic_unique == basic_total and performance_unique == performance_total:
                print(f"   ✅ 推荐作为主键（在两个表中都是唯一的）")
            elif basic_unique == basic_total or performance_unique == performance_total:
                print(f"   ⚠️  可能适合作为关联键（在其中一个表中唯一）")
            else:
                print(f"   ❌ 不是唯一字段，不适合作为关联键")
        
        print(f"\n✅ 分析完成！")
        return True
        
    except ImportError as e:
        print(f"❌ 导入错误：{str(e)}")
        print("\n💡 解决方案：")
        print("   请安装必要的Python库：")
        print("   pip install pandas openpyxl")
        return False
        
    except Exception as e:
        print(f"❌ 读取文件时出错：{str(e)}")
        print("\n💡 可能的原因：")
        print("   1. Excel文件格式不正确")
        print("   2. 文件被其他程序占用")
        print("   3. 文件损坏")
        return False

def main():
    """
    主函数
    """
    print("🚀 启动Excel字段分析工具...")
    
    # 检查当前目录
    current_dir = os.getcwd()
    print(f"📁 当前工作目录：{current_dir}")
    
    # 列出当前目录的Excel文件
    excel_files = [f for f in os.listdir('.') if f.endswith(('.xlsx', '.xls'))]
    if excel_files:
        print(f"📄 发现Excel文件：{excel_files}")
    else:
        print("⚠️  当前目录下没有发现Excel文件")
    
    # 执行分析
    success = analyze_excel_files()
    
    if success:
        print(f"\n🎉 分析成功完成！")
    else:
        print(f"\n💥 分析失败，请检查错误信息")
        sys.exit(1)

if __name__ == "__main__":
    main()
