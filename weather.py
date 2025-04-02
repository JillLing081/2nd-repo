import argparse
import requests
from typing import Optional, Dict, Any
import json
from datetime import datetime

class WeatherAPI:
    def __init__(self, api_key: str) -> None:
        """
        初始化天气API客户端
        :param api_key: OpenWeatherMap API密钥
        """
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        
    def get_temperature(self, city: str) -> Optional[Dict[str, Any]]:
        """
        获取指定城市的当前温度
        :param city: 城市名称
        :return: 包含温度信息的字典
        """
        try:
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric',  # 使用摄氏度
                'lang': 'zh_cn'     # 使用中文
            }
            
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()  # 检查请求是否成功
            
            data = response.json()
            
            # 提取需要的信息
            weather_info = {
                '城市': data['name'],
                '温度': f"{data['main']['temp']}°C",
                '体感温度': f"{data['main']['feels_like']}°C",
                '湿度': f"{data['main']['humidity']}%",
                '天气': data['weather'][0]['description'],
                '风速': f"{data['wind']['speed']} m/s",
                '更新时间': datetime.fromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M:%S')
            }
            
            return weather_info
            
        except requests.exceptions.RequestException as e:
            print(f"获取天气信息时出错: {str(e)}")
            return None
        except KeyError as e:
            print(f"解析天气数据时出错: {str(e)}")
            return None

def main() -> None:
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description='查询城市当前温度')
    parser.add_argument('city', type=str, help='要查询的城市名称')
    parser.add_argument('--api-key', type=str, help='OpenWeatherMap API密钥', 
                       default='YOUR_API_KEY_HERE')  # 替换为您的API密钥
    
    # 解析命令行参数
    args = parser.parse_args()
    
    # 创建天气API客户端
    weather_client = WeatherAPI(args.api_key)
    
    # 获取温度信息
    weather_info = weather_client.get_temperature(args.city)
    
    if weather_info:
        print("\n当前天气信息：")
        for key, value in weather_info.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    main() 