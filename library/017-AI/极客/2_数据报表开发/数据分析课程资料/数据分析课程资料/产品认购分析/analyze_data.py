import pandas as pd
import numpy as np

# 读取CSV文件
print("正在读取train.csv文件...")
df = pd.read_csv('train.csv')

print(f"数据表形状: {df.shape}")
print(f"共有 {df.shape[0]} 行数据，{df.shape[1]} 个字段")
print("\n" + "="*50)

# 显示字段基本信息
print("字段基本信息:")
print(df.info())

print("\n" + "="*50)

# 显示前几行数据
print("前5行数据:")
print(df.head())

print("\n" + "="*50)

# 字段含义分析
print("字段含义分析:")
print("="*30)

field_meanings = {
    'id': '客户唯一标识符',
    'age': '客户年龄',
    'job': '职业类型',
    'marital': '婚姻状况',
    'education': '教育水平',
    'default': '是否有违约记录',
    'housing': '是否有住房贷款',
    'loan': '是否有个人贷款',
    'contact': '联系方式类型',
    'month': '最后联系月份',
    'day_of_week': '最后联系星期几',
    'duration': '通话持续时间(秒)',
    'campaign': '本次营销活动联系次数',
    'pdays': '距离上次联系的天数(999表示从未联系过)',
    'previous': '之前营销活动联系次数',
    'poutcome': '之前营销活动的结果',
    'emp_var_rate': '就业变化率',
    'cons_price_index': '消费者价格指数',
    'cons_conf_index': '消费者信心指数',
    'lending_rate3m': '3个月贷款利率',
    'nr_employed': '就业人数',
    'subscribe': '是否认购产品(目标变量)'
}

for field in df.columns:
    print(f"{field:20} : {field_meanings.get(field, '未知字段')}")

print("\n" + "="*50)

# 显示各字段的数据类型和唯一值数量
print("各字段统计信息:")
for col in df.columns:
    unique_count = df[col].nunique()
    data_type = df[col].dtype
    print(f"{col:20} : 类型={str(data_type):10} 唯一值数量={unique_count:6}")

print("\n" + "="*50)

# 显示目标变量的分布
print("目标变量(subscribe)分布:")
print(df['subscribe'].value_counts())
print(f"认购率: {df['subscribe'].value_counts()['yes'] / len(df) * 100:.2f}%")

print("\n" + "="*50)

# 显示分类字段的唯一值
print("分类字段的唯一值:")
categorical_fields = ['job', 'marital', 'education', 'default', 'housing', 'loan', 
                     'contact', 'month', 'day_of_week', 'poutcome', 'subscribe']

for field in categorical_fields:
    if field in df.columns:
        print(f"\n{field}:")
        print(df[field].value_counts())

print("\n" + "="*50)

# 数值字段的统计信息
print("数值字段统计信息:")
numerical_fields = ['age', 'duration', 'campaign', 'pdays', 'previous', 
                   'emp_var_rate', 'cons_price_index', 'cons_conf_index', 
                   'lending_rate3m', 'nr_employed']

for field in numerical_fields:
    if field in df.columns:
        print(f"\n{field}:")
        print(df[field].describe())

print("\n" + "="*50)

# 检查缺失值
print("缺失值统计:")
missing_values = df.isnull().sum()
print(missing_values[missing_values > 0])

if missing_values.sum() == 0:
    print("数据中没有缺失值")

print("\n分析完成!")
