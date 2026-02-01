import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve
from sklearn.feature_selection import SelectKBest, f_classif
import warnings
warnings.filterwarnings('ignore')

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

print("开始构建产品认购预测模型...")

# 读取数据
df = pd.read_csv('train.csv')
print(f"数据形状: {df.shape}")

# 数据预处理
print("\n开始数据预处理...")

# 1. 处理分类变量
categorical_columns = ['job', 'marital', 'education', 'default', 'housing', 'loan', 
                      'contact', 'month', 'day_of_week', 'poutcome']

# 首先查看分类变量的唯一值
print("分类变量唯一值统计:")
for col in categorical_columns:
    print(f"{col}: {df[col].nunique()} 个唯一值")

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
print("特征列表:", feature_columns)

# 4. 准备训练数据
X = df[feature_columns]
y = df['target']

print(f"特征矩阵形状: {X.shape}")
print(f"目标变量分布: {y.value_counts()}")
print(f"认购率: {y.mean()*100:.2f}%")

# 5. 数据分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print(f"训练集大小: {X_train.shape}")
print(f"测试集大小: {X_test.shape}")

# 6. 特征标准化
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("\n开始训练多个分类模型...")

# 创建多个分类器
classifiers = {
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'Gradient Boosting': GradientBoostingClassifier(random_state=42),
    'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000),
    'Decision Tree': DecisionTreeClassifier(random_state=42),
    'SVM': SVC(random_state=42, probability=True)
}

# 存储模型结果
model_results = {}
feature_importance_data = []

# 训练和评估模型
for name, classifier in classifiers.items():
    print(f"\n训练 {name} 模型...")
    
    # 选择合适的特征（标准化或原始特征）
    if name in ['Logistic Regression', 'SVM']:
        X_train_model = X_train_scaled
        X_test_model = X_test_scaled
    else:
        X_train_model = X_train
        X_test_model = X_test
    
    # 训练模型
    classifier.fit(X_train_model, y_train)
    
    # 预测
    y_pred = classifier.predict(X_test_model)
    y_pred_proba = classifier.predict_proba(X_test_model)[:, 1]
    
    # 计算评估指标
    auc_score = roc_auc_score(y_test, y_pred_proba)
    
    # 交叉验证
    cv_scores = cross_val_score(classifier, X_train_model, y_train, cv=5, scoring='roc_auc')
    
    model_results[name] = {
        'classifier': classifier,
        'auc_score': auc_score,
        'cv_mean': cv_scores.mean(),
        'cv_std': cv_scores.std(),
        'predictions': y_pred,
        'probabilities': y_pred_proba
    }
    
    print(f"{name} - AUC: {auc_score:.4f}, CV AUC: {cv_scores.mean():.4f} (+/- {cv_scores.std()*2:.4f})")
    
    # 提取特征重要性
    if hasattr(classifier, 'feature_importances_'):
        importances = classifier.feature_importances_
        feature_names = feature_columns
        
        # 存储特征重要性数据
        for i, (feature, importance) in enumerate(zip(feature_names, importances)):
            feature_importance_data.append({
                'Model': name,
                'Feature': feature,
                'Importance': importance
            })

# 选择最佳模型
best_model_name = max(model_results.keys(), key=lambda x: model_results[x]['auc_score'])
best_model = model_results[best_model_name]['classifier']

print(f"\n最佳模型: {best_model_name}")
print(f"最佳模型 AUC: {model_results[best_model_name]['auc_score']:.4f}")

# 生成模型性能报告
print("\n生成模型性能报告...")
fig = plt.figure(figsize=(15, 10))

# 1. 模型性能比较
plt.subplot(2, 2, 1)
model_names = list(model_results.keys())
auc_scores = [model_results[name]['auc_score'] for name in model_names]
cv_means = [model_results[name]['cv_mean'] for name in model_names]
cv_stds = [model_results[name]['cv_std'] for name in model_names]

x = np.arange(len(model_names))
width = 0.35

plt.bar(x - width/2, auc_scores, width, label='Test AUC', alpha=0.8)
plt.bar(x + width/2, cv_means, width, label='CV AUC Mean', alpha=0.8)
plt.errorbar(x + width/2, cv_means, yerr=cv_stds, fmt='none', color='black', capsize=5)

plt.xlabel('模型')
plt.ylabel('AUC Score')
plt.title('模型性能比较', fontsize=14, fontweight='bold')
plt.xticks(x, model_names, rotation=45)
plt.legend()
plt.grid(axis='y', alpha=0.3)

# 添加数值标签
for i, (auc, cv_mean) in enumerate(zip(auc_scores, cv_means)):
    plt.text(i - width/2, auc + 0.01, f'{auc:.3f}', ha='center', va='bottom')
    plt.text(i + width/2, cv_mean + 0.01, f'{cv_mean:.3f}', ha='center', va='bottom')

# 2. 最佳模型的混淆矩阵
plt.subplot(2, 2, 2)
best_predictions = model_results[best_model_name]['predictions']
cm = confusion_matrix(y_test, best_predictions)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['未认购', '认购'], yticklabels=['未认购', '认购'])
plt.title(f'{best_model_name} 混淆矩阵', fontsize=14, fontweight='bold')
plt.ylabel('真实值')
plt.xlabel('预测值')

# 3. ROC曲线
plt.subplot(2, 2, 3)
colors = ['blue', 'red', 'green', 'orange', 'purple']
for i, (name, results) in enumerate(model_results.items()):
    fpr, tpr, _ = roc_curve(y_test, results['probabilities'])
    auc = results['auc_score']
    plt.plot(fpr, tpr, color=colors[i], lw=2, label=f'{name} (AUC = {auc:.3f})')

plt.plot([0, 1], [0, 1], color='black', lw=2, linestyle='--', alpha=0.5)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('假正率 (FPR)')
plt.ylabel('真正率 (TPR)')
plt.title('ROC曲线比较', fontsize=14, fontweight='bold')
plt.legend(loc="lower right")
plt.grid(alpha=0.3)

# 4. 特征重要性（最佳模型）
plt.subplot(2, 2, 4)
if hasattr(best_model, 'feature_importances_'):
    # 使用原始特征数据训练最佳模型获取特征重要性
    if best_model_name in ['Logistic Regression', 'SVM']:
        best_model.fit(X_train_scaled, y_train)
    else:
        best_model.fit(X_train, y_train)
    
    importances = best_model.feature_importances_
    feature_names = feature_columns
    
    # 创建特征重要性DataFrame
    feature_importance_df = pd.DataFrame({
        'feature': feature_names,
        'importance': importances
    }).sort_values('importance', ascending=True)
    
    # 只显示前15个最重要的特征
    top_features = feature_importance_df.tail(15)
    
    plt.barh(range(len(top_features)), top_features['importance'])
    plt.yticks(range(len(top_features)), top_features['feature'])
    plt.xlabel('特征重要性')
    plt.title(f'{best_model_name} 特征重要性 (Top 15)', fontsize=14, fontweight='bold')
    plt.grid(axis='x', alpha=0.3)
    
    # 添加数值标签
    for i, (idx, row) in enumerate(top_features.iterrows()):
        plt.text(row['importance'] + 0.001, i, f'{row["importance"]:.3f}', 
                va='center', fontsize=9)

plt.tight_layout()
plt.savefig('模型性能分析.png', dpi=300, bbox_inches='tight')
plt.show()

# 创建特征重要性详细分析
print("\n生成特征重要性详细分析...")

if feature_importance_data:
    # 创建特征重要性DataFrame
    importance_df = pd.DataFrame(feature_importance_data)
    
    # 计算平均重要性
    avg_importance = importance_df.groupby('Feature')['Importance'].mean().reset_index()
    avg_importance = avg_importance.sort_values('Importance', ascending=False)
    
    print("\n特征重要性排序 (按平均重要性):")
    print("="*50)
    for i, (_, row) in enumerate(avg_importance.iterrows(), 1):
        print(f"{i:2d}. {row['Feature']:25} : {row['Importance']:.4f}")
    
    # 创建特征重要性可视化
    fig2 = plt.figure(figsize=(15, 12))
    
    # 1. 所有模型的特征重要性对比
    plt.subplot(2, 2, 1)
    pivot_importance = importance_df.pivot(index='Feature', columns='Model', values='Importance')
    pivot_importance = pivot_importance.sort_values(best_model_name, ascending=True)
    
    # 只显示前15个最重要的特征
    top_features_pivot = pivot_importance.tail(15)
    
    top_features_pivot.plot(kind='barh', ax=plt.gca())
    plt.xlabel('特征重要性')
    plt.title('不同模型的特征重要性对比 (Top 15)', fontsize=14, fontweight='bold')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(axis='x', alpha=0.3)
    
    # 2. 最佳模型的特征重要性
    plt.subplot(2, 2, 2)
    best_model_importance = importance_df[importance_df['Model'] == best_model_name]
    best_model_importance = best_model_importance.sort_values('Importance', ascending=True)
    top_best_features = best_model_importance.tail(15)
    
    plt.barh(range(len(top_best_features)), top_best_features['Importance'])
    plt.yticks(range(len(top_best_features)), top_best_features['Feature'])
    plt.xlabel('特征重要性')
    plt.title(f'{best_model_name} 特征重要性详细分析', fontsize=14, fontweight='bold')
    plt.grid(axis='x', alpha=0.3)
    
    # 添加数值标签
    for i, (_, row) in enumerate(top_best_features.iterrows()):
        plt.text(row['Importance'] + 0.001, i, f'{row["Importance"]:.3f}', 
                va='center', fontsize=9)
    
    # 3. 特征重要性分布
    plt.subplot(2, 2, 3)
    plt.hist(avg_importance['Importance'], bins=20, alpha=0.7, edgecolor='black')
    plt.axvline(avg_importance['Importance'].mean(), color='red', linestyle='--', 
               label=f'平均值: {avg_importance["Importance"].mean():.3f}')
    plt.xlabel('特征重要性')
    plt.ylabel('频次')
    plt.title('特征重要性分布', fontsize=14, fontweight='bold')
    plt.legend()
    plt.grid(alpha=0.3)
    
    # 4. 累积重要性
    plt.subplot(2, 2, 4)
    cumulative_importance = avg_importance['Importance'].cumsum()
    cumulative_percentage = (cumulative_importance / cumulative_importance.iloc[-1]) * 100
    
    plt.plot(range(1, len(cumulative_percentage) + 1), cumulative_percentage, marker='o')
    plt.axhline(y=80, color='red', linestyle='--', alpha=0.7, label='80%重要性')
    plt.axhline(y=90, color='orange', linestyle='--', alpha=0.7, label='90%重要性')
    plt.xlabel('特征数量')
    plt.ylabel('累积重要性 (%)')
    plt.title('累积特征重要性', fontsize=14, fontweight='bold')
    plt.legend()
    plt.grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('特征重要性分析.png', dpi=300, bbox_inches='tight')
    plt.show()

# 生成分类报告
print(f"\n{best_model_name} 分类报告:")
print("="*50)
print(classification_report(y_test, model_results[best_model_name]['predictions'], 
                          target_names=['未认购', '认购']))

# 保存特征重要性数据
if feature_importance_data:
    importance_df.to_csv('特征重要性数据.csv', index=False, encoding='utf-8-sig')
    avg_importance.to_csv('平均特征重要性排序.csv', index=False, encoding='utf-8-sig')

print("\n模型分析完成！")
print(f"最佳模型: {best_model_name}")
print(f"最佳AUC: {model_results[best_model_name]['auc_score']:.4f}")

# 输出关键发现
print("\n关键发现:")
print("="*30)
if feature_importance_data:
    top_5_features = avg_importance.head(5)
    print("最重要的5个特征:")
    for i, (_, row) in enumerate(top_5_features.iterrows(), 1):
        print(f"{i}. {row['Feature']} (重要性: {row['Importance']:.4f})")
    
    # 分析特征类型
    duration_features = avg_importance[avg_importance['Feature'].str.contains('duration', case=False)]
    campaign_features = avg_importance[avg_importance['Feature'].str.contains('campaign', case=False)]
    economic_features = avg_importance[avg_importance['Feature'].str.contains('emp_var_rate|cons_price_index|cons_conf_index|lending_rate3m|nr_employed')]
    
    print(f"\n沟通时长相关特征平均重要性: {duration_features['Importance'].mean():.4f}")
    print(f"营销活动相关特征平均重要性: {campaign_features['Importance'].mean():.4f}")
    print(f"宏观经济特征平均重要性: {economic_features['Importance'].mean():.4f}")
