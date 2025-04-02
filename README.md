<<<<<<< HEAD
# 时间消耗分析器

这是一个用于分析Excel格式时间记录的工具，可以帮助您统计和分析时间消耗情况。

## 功能特点

- 从Excel文件读取时间记录数据
- 按类别统计时间消耗
- 生成时间分布饼图
- 提供每日时间消耗汇总

## 安装依赖

```bash
pip install -r requirements.txt
```

## Excel文件格式要求

您的Excel文件需要包含以下列：
- 日期
- 开始时间
- 结束时间
- 活动类别
- 具体内容

## 使用方法

1. 准备符合格式要求的Excel文件（默认名称为 `time_records.xlsx`）
2. 运行程序：
   ```bash
   python time_analyzer.py
   ```
3. 查看输出结果和生成的饼图

## 输出结果

程序会生成：
- 控制台输出的类别时间汇总
- 控制台输出的每日时间汇总
- 时间分布饼图（保存为 `time_distribution.png`） 
=======
# 2nd-repo
>>>>>>> 399c2a5c2b91515d8c7384762dea6dd07d4635da
