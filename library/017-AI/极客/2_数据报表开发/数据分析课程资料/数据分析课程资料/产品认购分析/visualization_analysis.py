import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib import rcParams
import warnings
warnings.filterwarnings('ignore')

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
print("正在读取数据...")
df = pd.read_csv('train.csv')

# 创建认购率计算函数
def calculate_subscription_rate(data, group_col, target_col='subscribe'):
    """计算认购率"""
    result = data.groupby(group_col)[target_col].apply(
        lambda x: (x == 'yes').sum() / len(x) * 100
    ).reset_index()
    result.columns = [group_col, 'subscription_rate']
    return result

# 设置图表样式
plt.style.use('seaborn-v0_8')
fig = plt.figure(figsize=(20, 24))

print("开始生成可视化图表...")

# 1. 不同职业的认购情况
print("1. 分析不同职业的认购情况...")
plt.subplot(4, 2, 1)
job_subscription = calculate_subscription_rate(df, 'job')
job_subscription = job_subscription.sort_values('subscription_rate', ascending=True)

# 创建水平柱状图
bars = plt.barh(range(len(job_subscription)), job_subscription['subscription_rate'])
plt.yticks(range(len(job_subscription)), job_subscription['job'])
plt.xlabel('认购率 (%)')
plt.title('不同职业的认购情况', fontsize=14, fontweight='bold')
plt.grid(axis='x', alpha=0.3)

# 添加数值标签
for i, bar in enumerate(bars):
    width = bar.get_width()
    plt.text(width + 0.1, bar.get_y() + bar.get_height()/2, 
             f'{width:.1f}%', ha='left', va='center', fontsize=10)

# 2. 联系方式的认购情况
print("2. 分析联系方式的认购情况...")
plt.subplot(4, 2, 2)
contact_subscription = calculate_subscription_rate(df, 'contact')
bars = plt.bar(contact_subscription['contact'], contact_subscription['subscription_rate'])
plt.ylabel('认购率 (%)')
plt.title('不同联系方式的认购情况', fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3)

# 添加数值标签
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.2, 
             f'{height:.1f}%', ha='center', va='bottom', fontsize=12)

# 3. 不同教育水平的认购情况
print("3. 分析不同教育水平的认购情况...")
plt.subplot(4, 2, 3)
education_subscription = calculate_subscription_rate(df, 'education')
education_subscription = education_subscription.sort_values('subscription_rate', ascending=True)

bars = plt.barh(range(len(education_subscription)), education_subscription['subscription_rate'])
plt.yticks(range(len(education_subscription)), education_subscription['education'])
plt.xlabel('认购率 (%)')
plt.title('不同教育水平的认购情况', fontsize=14, fontweight='bold')
plt.grid(axis='x', alpha=0.3)

# 添加数值标签
for i, bar in enumerate(bars):
    width = bar.get_width()
    plt.text(width + 0.1, bar.get_y() + bar.get_height()/2, 
             f'{width:.1f}%', ha='left', va='center', fontsize=10)

# 4. 婚姻状况的认购情况
print("4. 分析婚姻状况的认购情况...")
plt.subplot(4, 2, 4)
marital_subscription = calculate_subscription_rate(df, 'marital')
bars = plt.bar(marital_subscription['marital'], marital_subscription['subscription_rate'])
plt.ylabel('认购率 (%)')
plt.title('不同婚姻状况的认购情况', fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3)

# 添加数值标签
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.2, 
             f'{height:.1f}%', ha='center', va='bottom', fontsize=12)

# 5. 房贷情况的认购情况
print("5. 分析房贷情况的认购情况...")
plt.subplot(4, 2, 5)
housing_subscription = calculate_subscription_rate(df, 'housing')
bars = plt.bar(housing_subscription['housing'], housing_subscription['subscription_rate'])
plt.ylabel('认购率 (%)')
plt.title('不同房贷情况的认购情况', fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3)

# 添加数值标签
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.2, 
             f'{height:.1f}%', ha='center', va='bottom', fontsize=12)

# 6. 个人贷款情况的认购情况
print("6. 分析个人贷款情况的认购情况...")
plt.subplot(4, 2, 6)
loan_subscription = calculate_subscription_rate(df, 'loan')
bars = plt.bar(loan_subscription['loan'], loan_subscription['subscription_rate'])
plt.ylabel('认购率 (%)')
plt.title('不同个人贷款情况的认购情况', fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3)

# 添加数值标签
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.2, 
             f'{height:.1f}%', ha='center', va='bottom', fontsize=12)

# 7. 违约记录的认购情况
print("7. 分析违约记录的认购情况...")
plt.subplot(4, 2, 7)
default_subscription = calculate_subscription_rate(df, 'default')
bars = plt.bar(default_subscription['default'], default_subscription['subscription_rate'])
plt.ylabel('认购率 (%)')
plt.title('不同违约记录的认购情况', fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3)

# 添加数值标签
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.2, 
             f'{height:.1f}%', ha='center', va='bottom', fontsize=12)

# 8. 星期几的认购情况
print("8. 分析星期几的认购情况...")
plt.subplot(4, 2, 8)
day_subscription = calculate_subscription_rate(df, 'day_of_week')
day_order = ['mon', 'tue', 'wed', 'thu', 'fri']
day_subscription = day_subscription.set_index('day_of_week').reindex(day_order).reset_index()

bars = plt.bar(day_subscription['day_of_week'], day_subscription['subscription_rate'])
plt.ylabel('认购率 (%)')
plt.title('不同星期几的认购情况', fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3)

# 添加数值标签
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.2, 
             f'{height:.1f}%', ha='center', va='bottom', fontsize=12)

plt.tight_layout()
plt.savefig('认购情况分析图表.png', dpi=300, bbox_inches='tight')
plt.show()

print("基础分析图表已生成！")

# 创建第二个图表 - 沟通时长分析
print("\n开始生成沟通时长分析图表...")

fig2 = plt.figure(figsize=(20, 12))

# 1. 沟通时长分组的认购情况
print("1. 分析沟通时长分组的认购情况...")
plt.subplot(2, 2, 1)

# 将沟通时长分组
df['duration_group'] = pd.cut(df['duration'], 
                             bins=[0, 300, 600, 1200, 2400, float('inf')], 
                             labels=['0-5分钟', '5-10分钟', '10-20分钟', '20-40分钟', '40分钟以上'])

duration_subscription = calculate_subscription_rate(df, 'duration_group')
bars = plt.bar(range(len(duration_subscription)), duration_subscription['subscription_rate'])
plt.xticks(range(len(duration_subscription)), duration_subscription['duration_group'], rotation=45)
plt.ylabel('认购率 (%)')
plt.title('不同沟通时长的认购情况', fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3)

# 添加数值标签
for i, bar in enumerate(bars):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.2, 
             f'{height:.1f}%', ha='center', va='bottom', fontsize=11)

# 2. 活动中联系次数的认购情况
print("2. 分析活动中联系次数的认购情况...")
plt.subplot(2, 2, 2)

# 将联系次数分组
df['campaign_group'] = pd.cut(df['campaign'], 
                             bins=[0, 1, 2, 3, 5, float('inf')], 
                             labels=['1次', '2次', '3次', '4-5次', '5次以上'])

campaign_subscription = calculate_subscription_rate(df, 'campaign_group')
bars = plt.bar(range(len(campaign_subscription)), campaign_subscription['subscription_rate'])
plt.xticks(range(len(campaign_subscription)), campaign_subscription['campaign_group'])
plt.ylabel('认购率 (%)')
plt.title('不同联系次数的认购情况', fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3)

# 添加数值标签
for i, bar in enumerate(bars):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.2, 
             f'{height:.1f}%', ha='center', va='bottom', fontsize=11)

# 3. 沟通时长 vs 联系次数的热力图
print("3. 生成沟通时长与联系次数的认购率热力图...")
plt.subplot(2, 2, 3)

# 创建交叉表
pivot_table = df.pivot_table(values='subscribe', 
                            index='duration_group', 
                            columns='campaign_group', 
                            aggfunc=lambda x: (x == 'yes').mean() * 100)

# 绘制热力图
sns.heatmap(pivot_table, annot=True, fmt='.1f', cmap='YlOrRd', 
            cbar_kws={'label': '认购率 (%)'})
plt.title('沟通时长与联系次数的认购率热力图', fontsize=14, fontweight='bold')
plt.xlabel('联系次数')
plt.ylabel('沟通时长')

# 4. 沟通时长分布
print("4. 生成沟通时长分布图...")
plt.subplot(2, 2, 4)

# 绘制沟通时长的分布
plt.hist(df['duration'], bins=50, alpha=0.7, edgecolor='black')
plt.axvline(df['duration'].mean(), color='red', linestyle='--', 
           label=f'平均时长: {df["duration"].mean():.0f}秒')
plt.xlabel('沟通时长 (秒)')
plt.ylabel('频次')
plt.title('沟通时长分布', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(alpha=0.3)

plt.tight_layout()
plt.savefig('沟通时长分析图表.png', dpi=300, bbox_inches='tight')
plt.show()

print("沟通时长分析图表已生成！")

# 生成详细的数据报告
print("\n生成详细分析报告...")

# 创建分析报告
report_data = []

# 职业分析
job_analysis = df.groupby('job')['subscribe'].apply(lambda x: (x == 'yes').sum() / len(x) * 100).reset_index()
job_analysis.columns = ['类别', '认购率']
job_analysis['维度'] = '职业'
report_data.append(job_analysis)

# 联系方式分析
contact_analysis = df.groupby('contact')['subscribe'].apply(lambda x: (x == 'yes').sum() / len(x) * 100).reset_index()
contact_analysis.columns = ['类别', '认购率']
contact_analysis['维度'] = '联系方式'
report_data.append(contact_analysis)

# 教育水平分析
education_analysis = df.groupby('education')['subscribe'].apply(lambda x: (x == 'yes').sum() / len(x) * 100).reset_index()
education_analysis.columns = ['类别', '认购率']
education_analysis['维度'] = '教育水平'
report_data.append(education_analysis)

# 婚姻状况分析
marital_analysis = df.groupby('marital')['subscribe'].apply(lambda x: (x == 'yes').sum() / len(x) * 100).reset_index()
marital_analysis.columns = ['类别', '认购率']
marital_analysis['维度'] = '婚姻状况'
report_data.append(marital_analysis)

# 房贷分析
housing_analysis = df.groupby('housing')['subscribe'].apply(lambda x: (x == 'yes').sum() / len(x) * 100).reset_index()
housing_analysis.columns = ['类别', '认购率']
housing_analysis['维度'] = '房贷情况'
report_data.append(housing_analysis)

# 个人贷款分析
loan_analysis = df.groupby('loan')['subscribe'].apply(lambda x: (x == 'yes').sum() / len(x) * 100).reset_index()
loan_analysis.columns = ['类别', '认购率']
loan_analysis['维度'] = '个人贷款'
report_data.append(loan_analysis)

# 违约记录分析
default_analysis = df.groupby('default')['subscribe'].apply(lambda x: (x == 'yes').sum() / len(x) * 100).reset_index()
default_analysis.columns = ['类别', '认购率']
default_analysis['维度'] = '违约记录'
report_data.append(default_analysis)

# 星期几分析
day_analysis = df.groupby('day_of_week')['subscribe'].apply(lambda x: (x == 'yes').sum() / len(x) * 100).reset_index()
day_analysis.columns = ['类别', '认购率']
day_analysis['维度'] = '星期几'
report_data.append(day_analysis)

# 合并所有分析结果
final_report = pd.concat(report_data, ignore_index=True)
final_report = final_report[['维度', '类别', '认购率']].sort_values(['维度', '认购率'], ascending=[True, False])

# 保存报告
final_report.to_csv('认购情况详细分析报告.csv', index=False, encoding='utf-8-sig')

print("分析完成！")
print(f"总体认购率: {df['subscribe'].value_counts()['yes'] / len(df) * 100:.2f}%")
print("\n各维度认购率排序（前10名）:")
print(final_report.head(10).to_string(index=False))

print("\n各维度认购率排序（后10名）:")
print(final_report.tail(10).to_string(index=False))
