import json
import sys

import requests

'''
下载今后几天的天气预报，并以纯文本打印出来
总的来说，该程序将执行以下操作： 
•  从命令行读取请求的位置。 
•  从 OpenWeatherMap.org 下载 JSON 天气数据。 
•  将 JSON 数据字符串转换成 Python 的数据结构。 
•  打印今天和未来两天的天气。 
因此，代码需要完成以下任务： 
•  连接 sys.argv 中的字符串，得到位置。 
•  调用 requests.get()，下载天气数据。 
•  调用 json.loads()，将 JSON 数据转换为 Python 数据结构。 
•  打印天气预报。 
'''







if __name__ == '__main__':
    # •  连接 sys.argv 中的字符串，得到位置。
    if len(sys.argv) == 2:
        sys.argv[1]
    else:
        print('use:quickWeather.py city')

    # •  调用 requests.get()，下载天气数据。
    url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)
    # •  调用 json.loads()，将 JSON 数据转换为 Python 数据结构。

    # •  打印天气预报。