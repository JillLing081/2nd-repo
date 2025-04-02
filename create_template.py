import pandas as pd
from datetime import datetime, timedelta

def create_excel_template():
    # 创建示例数据
    data = {
        '日期': [
            '2024-03-15',
            '2024-03-15',
            '2024-03-15',
            '2024-03-16',
            '2024-03-16'
        ],
        '开始时间': [
            '2024-03-15 09:00:00',
            '2024-03-15 11:30:00',
            '2024-03-15 14:00:00',
            '2024-03-16 09:30:00',
            '2024-03-16 14:00:00'
        ],
        '结束时间': [
            '2024-03-15 11:00:00',
            '2024-03-15 12:30:00',
            '2024-03-15 17:30:00',
            '2024-03-16 12:00:00',
            '2024-03-16 18:00:00'
        ],
        '活动类别': [
            '工作',
            '休息',
            '学习',
            '会议',
            '项目开发'
        ],
        '具体内容': [
            '处理邮件和日常工作',
            '午休',
            'Python编程学习',
            '团队周会',
            '开发新功能模块'
        ]
    }
    
    # 创建DataFrame
    df = pd.DataFrame(data)
    
    # 设置Excel写入器
    writer = pd.ExcelWriter('time_records_template.xlsx', engine='openpyxl')
    
    # 写入数据
    df.to_excel(writer, index=False, sheet_name='时间记录')
    
    # 获取工作表
    worksheet = writer.sheets['时间记录']
    
    # 调整列宽
    worksheet.column_dimensions['A'].width = 12  # 日期
    worksheet.column_dimensions['B'].width = 20  # 开始时间
    worksheet.column_dimensions['C'].width = 20  # 结束时间
    worksheet.column_dimensions['D'].width = 15  # 活动类别
    worksheet.column_dimensions['E'].width = 30  # 具体内容
    
    # 保存文件
    writer.close()
    
    print("模板文件 'time_records_template.xlsx' 已创建成功！")
    print("\n模板包含以下示例数据：")
    print(df)

if __name__ == "__main__":
    create_excel_template() 