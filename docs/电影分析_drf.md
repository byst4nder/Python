```python
import csv
import pandas as pd
import tushare as ts
from pyecharts import Funnel, Bar, Line

month_list = ['20180101', '20180201', '20180301', '20180401', '20180501',
              '20180601', '20180701', '20180801', '20180901', '20181001']

class MovieAnalyse:

    def __init__(self,month_list):
        month_list = month_list

    def get_pro(self):
        """
        获取pro
        :return:pro
        """
        pro = ts.pro_api('892849075ca78931c825284506de72fc4e0622ae0e800ab7fb0c5227')
        return pro

    def get_data(self):
        """
        返回所有月合并的电影数据
        :param month:
        :return:
        """
        pro = self.get_pro()
        lm = []
        for m in self.month_list:
            dfm = pro.bo_monthly(date=m)
            lm.append(dfm)
        # 获取9个df合并后dataframe
        res = pd.concat(lm, axis=0, ignore_index=True)
        return res

    def top_amount(self):
        """
        获取top10电影票房
        :param
        :return:
        """
        res = self.get_data()
        # 对票房数据进行分组排序
        reqc = res.groupby('name')['month_amount']
        reqc = reqc.sum()
        # 对分组后的数据根据月票房从大到小进行排序
        reqc = reqc.sort_values(ascending=False)
        reqc.to_csv( "top10_113.csv")

        # 读取csv文件
        csv_file = csv.reader(open('top10_113.csv', 'r'))
        # 电影名字列表
        name_list = []
        # 电影票房列表
        amount = []
        num = 0
        for m in csv_file:
            num += 1
            if m[0] != "其他":
                name_list.append(m[0])
                amount.append(m[1])
            if num == 11:
                break
        # 生成echarts表
        bar = Bar("票房最高的电影Top10")
        bar.add("电影票房",
                name_list, amount,
                is_more_utils=True)
        bar.render(path="票房top10.html", )
        return '票房top10数据生成完毕'

    def top_renqi(self):
        """
        获取人气top10图表
        :return:
        """
        res = self.get_data()
        test = res.drop_duplicates(subset=['name'], keep="first")
        # 根据口碑指数排名top10
        sort_p_pc = test.sort_values(by="p_pc", ascending=False)[0:11]
        # 存储为csv文件
        sort_p_pc.to_csv("p_pc.csv")
        # 读取csv文件
        csv_file = csv.reader(open('p_pc.csv', 'r'))

        name_list = []
        pc_list = []
        for cs in csv_file:
            # 去掉数据
            if cs[1] == "date":
                continue
            name_list.append(cs[2])
            pc_list.append(cs[7])

        bar = Bar("人气的电影Top10")
        bar.add("电影票房",
                name_list, pc_list,
                is_more_utils=True)
        bar.render(path="人气top10.html", )
        return "人气电影topok"

    def xing_jia_bi(self):
        """
        获取性价比电影
        :return:
        """
        res = self.get_data()
        test = res.drop_duplicates(subset=['name'], keep="first")
        # 根据口碑指数排名top10
        sort_wom_index = test.sort_values(by="wom_index", ascending=False)[0:11]
        # 对上面根据价格进行排序
        sort_price = sort_wom_index.sort_values(by="avg_price", ascending=True)
        sort_price.to_csv("wom_price11.csv")

        movie_list = []
        price_list = []
        wom_list = []
        # 读取csv文件
        csv_file = csv.reader(open('wom_price11.csv', 'r'))
        # 生成echarts表
        for wp in csv_file:
            if wp[1] == "date":
                continue
            movie_list.append(wp[2])
            price_list.append(wp[4])
            wom_list.append(wp[8])
        line = Line("性价比（价格/口碑指数）")
        line.add("平均价格价格", movie_list, price_list)
        line.add("口碑指数", movie_list, wom_list)
        line.render(path="性价比111.html", )

    def dan_wang(self):
        """
        获取淡旺季电影
        :return:
        """
        pro = self.get_pro()
        month_l = []
        amount_l = []

        for month in self.month_list:
            df = pro.bo_monthly(date=month)
            month_amount = df['month_amount'].sum()
            mon = f"{month[4:6]}月份"
            month_l.append(mon)
            amount_l.append(month_amount)

        funnel = Funnel("")
        funnel.add(
            "商品",
            month_l,
            amount_l,
            is_label_show=True,
            label_pos="inside",
            label_text_color="#fff",
        )
        funnel.render(path="淡旺季.html", )
```

1.票房最高的电影Top10

得出票房最高的是红海行动

```python
movie = MovieAnalyse(month_list)
movie.top_amount()
```

![](C:\Users\10499\Desktop\movie_\票房top10.png)

2.人气最高的电影top10

人气最高的是红海行动

```
movie.top_renqi()
```

![](C:\Users\10499\Desktop\movie_\人气top10.png)

3).性价比最好的电影(根据价格和口碑指数)

价格与口碑指数之间距离越小，性价比越高，得出电影奇迹男孩性价比最高

```python
movie.xing_jia_bi()
```

![](C:\Users\10499\Desktop\movie_\性价比.png)

4.找出淡季和旺季

根据漏斗图得出2018年2月份电影是旺季9月份电影是淡季

```python
movie.dan_wang()
```

![](C:\Users\10499\Desktop\movie_\淡旺季.png)

```txt
requirements.txt
python == 3.6.3
pandas == 0.20.3
pyecharts == 0.5.6
```

