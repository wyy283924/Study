import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
import warnings
warnings.filterwarnings('ignore')

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

print("开始逻辑回归特征系数分析...")

# 读取数据
df = pd.read_csv('train.csv')
print(f"数据形状: {df.shape}")

# 数据预处理
print("\n开始数据预处理...")

# 1. 处理分类变量
categorical_columns = ['job', 'marital', 'education', 'default', 'housing', 'loan', 
                      'contact', 'month', 'day_of_week', 'poutcome']

# 对分类变量进行标签编码
label_encoders = {}
for col in categorical_columns:
    le = LabelEncoder()
    df[col + '_encoded'] = le.fit_transform(df[col])
    label_encoders[col] = le

# 2. 处理目标变量
df['target'] = (df['subscribe'] == 'yes').astype(int)

# 3. 选择特征
feature_columns = ['age', 'duration', 'campaign', 'pdays', 'previous', 
                  'emp_var_rate', 'cons_price_index', 'cons_conf_index', 
                  'lending_rate3m', 'nr_employed']

# 添加编码后的分类变量
for col in categorical_columns:
    feature_columns.append(col + '_encoded')

print(f"选择的特征数量: {len(feature_columns)}")

# 4. 准备训练数据
X = df[feature_columns]
y = df['target']

print(f"特征矩阵形状: {X.shape}")
print(f"目标变量分布: {y.value_counts()}")
print(f"认购率: {y.mean()*100:.2f}%")

# 5. 数据分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# 6. 特征标准化（逻辑回归需要标准化）
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("\n训练逻辑回归模型...")

# 创建逻辑回归模型
logistic_model = LogisticRegression(random_state=42, max_iter=1000)

# 训练模型
logistic_model.fit(X_train_scaled, y_train)

# 预测
y_pred = logistic_model.predict(X_test_scaled)
y_pred_proba = logistic_model.predict_proba(X_test_scaled)[:, 1]

# 计算评估指标
auc_score = roc_auc_score(y_test, y_pred_proba)
print(f"逻辑回归 AUC Score: {auc_score:.4f}")

# 获取特征系数
coefficients = logistic_model.coef_[0]
feature_names = feature_columns

# 创建特征系数DataFrame
coefficients_df = pd.DataFrame({
    'feature': feature_names,
    'coefficient': coefficients,
    'abs_coefficient': np.abs(coefficients)
})

# 按绝对值排序
coefficients_df = coefficients_df.sort_values('abs_coefficient', ascending=True)

print("\n逻辑回归特征系数分析:")
print("="*60)
print(f"{'特征名称':<25} {'系数':<12} {'绝对值':<10} {'方向':<8}")
print("-"*60)

for _, row in coefficients_df.iterrows():
    direction = "正向" if row['coefficient'] > 0 else "负向"
    print(f"{row['feature']:<25} {row['coefficient']:<12.4f} {row['abs_coefficient']:<10.4f} {direction:<8}")

# 创建可视化
fig = plt.figure(figsize=(16, 12))

# 1. 特征系数柱状图（按绝对值排序，保留正负号）
plt.subplot(2, 2, 1)

# 准备数据
y_pos = np.arange(len(coefficients_df))
coefficients = coefficients_df['coefficient'].values
feature_names = coefficients_df['feature'].values

# 创建颜色映射：正数为蓝色，负数为红色
colors = ['red' if c < 0 else 'blue' for c in coefficients]

# 绘制柱状图
bars = plt.barh(y_pos, coefficients, color=colors, alpha=0.7, edgecolor='black', linewidth=0.5)

plt.yticks(y_pos, feature_names)
plt.xlabel('特征系数')
plt.title('逻辑回归特征系数分析（按绝对值排序）', fontsize=14, fontweight='bold')
plt.grid(axis='x', alpha=0.3)

# 添加零线
plt.axvline(x=0, color='black', linestyle='-', linewidth=1)

# 添加数值标签
for i, (bar, coeff) in enumerate(zip(bars, coefficients)):
    width = bar.get_width()
    if width >= 0:
        plt.text(width + 0.01, bar.get_y() + bar.get_height()/2, 
                f'{coeff:.3f}', ha='left', va='center', fontsize=9)
    else:
        plt.text(width - 0.01, bar.get_y() + bar.get_height()/2, 
                f'{coeff:.3f}', ha='right', va='center', fontsize=9)

# 添加图例
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor='blue', alpha=0.7, label='正向影响（促进认购）'),
                  Patch(facecolor='red', alpha=0.7, label='负向影响（抑制认购）')]
plt.legend(handles=legend_elements, loc='lower right')

# 2. 特征系数绝对值排序
plt.subplot(2, 2, 2)
abs_coefficients = coefficients_df['abs_coefficient'].values

plt.barh(y_pos, abs_coefficients, alpha=0.7, color='green', edgecolor='black', linewidth=0.5)
plt.yticks(y_pos, feature_names)
plt.xlabel('特征系数绝对值')
plt.title('特征重要性（按系数绝对值排序）', fontsize=14, fontweight='bold')
plt.grid(axis='x', alpha=0.3)

# 添加数值标签
for i, (bar, abs_coeff) in enumerate(zip(bars, abs_coefficients)):
    width = bar.get_width()
    plt.text(width + 0.01, bar.get_y() + bar.get_height()/2, 
            f'{abs_coeff:.3f}', ha='left', va='center', fontsize=9)

# 3. 正向和负向系数分布
plt.subplot(2, 2, 3)

positive_coeffs = coefficients_df[coefficients_df['coefficient'] > 0]['coefficient']
negative_coeffs = coefficients_df[coefficients_df['coefficient'] < 0]['coefficient']

plt.hist(positive_coeffs, bins=10, alpha=0.7, label=f'正向系数 (n={len(positive_coeffs)})', color='blue')
plt.hist(negative_coeffs, bins=10, alpha=0.7, label=f'负向系数 (n={len(negative_coeffs)})', color='red')
plt.xlabel('系数值')
plt.ylabel('频次')
plt.title('特征系数分布', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(alpha=0.3)

# 4. 模型性能评估
plt.subplot(2, 2, 4)

# 混淆矩阵
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['未认购', '认购'], yticklabels=['未认购', '认购'])
plt.title(f'逻辑回归混淆矩阵\nAUC = {auc_score:.4f}', fontsize=14, fontweight='bold')
plt.ylabel('真实值')
plt.xlabel('预测值')

plt.tight_layout()
plt.savefig('逻辑回归特征系数分析.png', dpi=300, bbox_inches='tight')
plt.show()

# 生成详细分析报告
print("\n生成详细分析报告...")

# 创建正向和负向影响的分析
positive_features = coefficients_df[coefficients_df['coefficient'] > 0].sort_values('coefficient', ascending=False)
negative_features = coefficients_df[coefficients_df['coefficient'] < 0].sort_values('coefficient', ascending=True)

print("\n正向影响特征（促进认购）:")
print("="*40)
for _, row in positive_features.iterrows():
    print(f"{row['feature']:<25} : {row['coefficient']:.4f}")

print("\n负向影响特征（抑制认购）:")
print("="*40)
for _, row in negative_features.iterrows():
    print(f"{row['feature']:<25} : {row['coefficient']:.4f}")

# 创建特征解释
feature_explanations = {
    'duration': '沟通时长 - 正系数表示沟通时间越长，认购概率越高',
    'emp_var_rate': '就业变化率 - 正系数表示就业环境改善促进认购',
    'pdays': '距离上次联系天数 - 负系数表示联系间隔越短，认购概率越高',
    'month_encoded': '联系月份 - 系数表示不同月份的认购倾向',
    'lending_rate3m': '3个月贷款利率 - 负系数表示利率越低，认购概率越高',
    'age': '年龄 - 系数表示不同年龄段的认购倾向',
    'campaign': '本次联系次数 - 负系数表示联系次数过多可能降低认购率',
    'cons_conf_index': '消费者信心指数 - 正系数表示信心越高，认购概率越高',
    'cons_price_index': '消费者价格指数 - 负系数表示通胀越低，认购概率越高',
    'nr_employed': '就业人数 - 正系数表示就业人数越多，认购概率越高'
}

print("\n特征系数解释:")
print("="*50)
for feature, explanation in feature_explanations.items():
    if feature in coefficients_df['feature'].values:
        coeff = coefficients_df[coefficients_df['feature'] == feature]['coefficient'].iloc[0]
        print(f"{feature:<20} (系数: {coeff:>7.4f}) : {explanation}")

# 保存分析结果
coefficients_df.to_csv('逻辑回归特征系数.csv', index=False, encoding='utf-8-sig')

print(f"\n逻辑回归分析完成！")
print(f"模型AUC: {auc_score:.4f}")
print(f"正向影响特征数量: {len(positive_features)}")
print(f"负向影响特征数量: {len(negative_features)}")

# 输出分类报告
print(f"\n逻辑回归分类报告:")
print("="*50)
print(classification_report(y_test, y_pred, target_names=['未认购', '认购']))
