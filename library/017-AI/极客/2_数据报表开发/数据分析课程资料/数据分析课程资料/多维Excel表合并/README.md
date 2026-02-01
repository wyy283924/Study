# Excel文件字段分析工具

这个工具用于分析员工基本信息表和员工绩效表的字段结构，帮助您了解两个Excel表的对应关系。

## 文件说明

- `excel_field_analyzer.py` - 主要的分析脚本（推荐使用）
- `simple_excel_reader.py` - 简化版分析脚本
- `excel_reader.py` - 详细版分析脚本
- `requirements.txt` - Python依赖包列表
- `run_excel_reader.bat` - Windows批处理文件

## 使用方法

### 方法1：直接运行Python脚本（推荐）

1. 确保Python已安装
2. 安装依赖包：
   ```bash
   pip install -r requirements.txt
   ```
   或者手动安装：
   ```bash
   pip install pandas openpyxl
   ```

3. 运行分析脚本：
   ```bash
   python excel_field_analyzer.py
   ```

### 方法2：使用批处理文件（Windows）

双击运行 `run_excel_reader.bat` 文件

## 功能特性

- 📊 显示两个Excel文件的基本信息（行数、列数）
- 📋 列出所有字段名称和数据类型
- 👀 预览前几行数据
- 🔍 分析两个表的共同字段和独有字段
- 🔑 识别可能的关联键字段
- ✅ 提供详细的错误信息和解决建议

## 输出示例

脚本会输出以下信息：

1. **基本信息表分析**
   - 数据形状（行数×列数）
   - 所有列名
   - 数据类型
   - 前3行数据预览

2. **绩效表分析**
   - 同上

3. **字段对比分析**
   - 共同字段
   - 仅在基本信息表中的字段
   - 仅在绩效表中的字段

4. **关联键分析**
   - 分析哪些字段适合作为两个表的关联键
   - 显示每个字段的唯一值数量

## 注意事项

- 确保Excel文件在当前目录下
- 文件名必须是：`员工基本信息表.xlsx` 和 `员工绩效表.xlsx`
- 如果遇到编码问题，请使用UTF-8编码运行脚本

## 故障排除

如果遇到问题，请检查：

1. Python是否正确安装
2. 依赖包是否已安装（pandas, openpyxl）
3. Excel文件是否存在且未被占用
4. 文件格式是否正确（.xlsx格式）
