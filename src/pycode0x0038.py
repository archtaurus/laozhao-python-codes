#!/usr/bin/env python
# coding: utf-8
"""老赵的Python代码碎片之一

文件: pycode0x0038.py
功能: 一个天气API的调用函数
许可: General Public License
作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
时间: 2017/01/11 14:10:14
"""


def get_weather_info(location, apikey=None, units='metric', lang='zh_cn'):
    if not apikey or len(apikey) != 32:
        raise ValueError('please get valid apikey from openweathermap.org.')
    import requests
    locations = {'nanjing': 1799962, 'xiaolingwei': 1790100}
    location = locations.get(location, location)
    query = {'query': 'id' if isinstance(location, int) else 'q',
             'city': location, 'apikey': apikey, 'units': units, 'lang': lang}
    api_url = ('http://api.openweathermap.org/data/2.5/weather?'
               '{query}={city}&appid={apikey}&units={units}&lang={lang}').format(**query)
    icon_url = 'http://openweathermap.org/img/w/{}.png'
    data = requests.get(api_url).json()
    return dict(latitude=data['coord']['lat'],
                longitude=data['coord']['lon'],
                datetime=data['dt'],
                sunrise=data['sys']['sunrise'],
                sunset=data['sys']['sunset'],
                weather=data['weather'][0]['description'],
                icon=icon_url.format(data['weather'][0]['icon']),
                cloudiness=data['clouds']['all'],
                humidity=data['main']['humidity'],
                pressure=data['main']['pressure'],  # hPa
                temperature=data['main']['temp'],
                wind_direction=data['wind']['deg'],
                wind_speed=data['wind']['speed'],  # meter/second
                base=data['base'], cod=data['cod'], visibility=data['visibility'])
