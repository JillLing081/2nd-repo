import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib as mpl
from typing import Optional, Dict, Any, List, Union
from pathlib import Path

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

class TimeAnalyzer:
    def __init__(self, excel_file: Union[str, Path]) -> None:
        """
        初始化时间分析器
        :param excel_file: Excel文件路径
        """
        self.excel_file = excel_file
        self.df: Optional[pd.DataFrame] = None
        
    def load_data(self) -> None:
        """
        加载Excel数据
        假设Excel文件包含以下列：
        - 日期
        - 开始时间
        - 结束时间
        - 活动类别
        - 具体内容
        """
        try:
            self.df = pd.read_excel(self.excel_file)
            # 将时间列转换为datetime类型
            self.df['开始时间'] = pd.to_datetime(self.df['开始时间'])
            self.df['结束时间'] = pd.to_datetime(self.df['结束时间'])
            # 计算持续时间（小时）
            self.df['持续时间'] = (self.df['结束时间'] - self.df['开始时间']).dt.total_seconds() / 3600
            print("数据加载成功！")
        except Exception as e:
            print(f"加载数据时出错: {str(e)}")
            
    def analyze_by_category(self) -> Optional[pd.DataFrame]:
        """
        按类别分析时间消耗
        :return: 包含类别时间汇总的DataFrame
        """
        if self.df is None:
            print("请先加载数据")
            return None
            
        # 按类别汇总时间
        category_summary = self.df.groupby('活动类别')['持续时间'].agg(['sum', 'count'])
        return category_summary
    
    def plot_category_distribution(self) -> None:
        """
        绘制类别时间分布饼图
        """
        if self.df is None:
            print("请先加载数据")
            return
            
        category_summary = self.analyze_by_category()
        if category_summary is None:
            return
        
        plt.figure(figsize=(10, 6))
        plt.pie(category_summary['sum'], labels=category_summary.index, autopct='%1.1f%%')
        plt.title('时间消耗类别分布', fontsize=12, pad=20)
        plt.savefig('time_distribution.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("饼图已保存为 'time_distribution.png'")
        
    def get_daily_summary(self) -> Optional[pd.Series]:
        """
        获取每日时间消耗汇总
        :return: 包含每日时间汇总的Series
        """
        if self.df is None:
            print("请先加载数据")
            return None
            
        # 添加日期列
        self.df['日期'] = self.df['开始时间'].dt.date
        daily_summary = self.df.groupby('日期')['持续时间'].sum()
        return daily_summary

def main() -> None:
    # 使用示例
    analyzer = TimeAnalyzer('time_records_template.xlsx')
    analyzer.load_data()
    
    # 获取类别汇总
    category_summary = analyzer.analyze_by_category()
    print("\n类别时间汇总：")
    print(category_summary)
    
    # 生成饼图
    analyzer.plot_category_distribution()
    
    # 获取每日汇总
    daily_summary = analyzer.get_daily_summary()
    print("\n每日时间汇总：")
    print(daily_summary)

if __name__ == "__main__":
    main() 