
import openpyxl
import pprint

'''
在这个项目中，你要编写一个脚本，从人口普查电子表格文件中读取数据，并
在几秒钟内计算出每个县的统计值。
下面是程序要做的事：
•  从 Excel 电子表格中读取数据。
•  计算每个县中普查区的数目。
•  计算每个县的总人口。
•  打印结果。
这意味着代码需要完成下列任务：
•  用 openpyxl 模块打开 Excel 文档并读取单元格。
•  计算所有普查区和人口数据，将它保存到一个数据结构中。
•  利用 pprint 模块，将该数据结构写入一个扩展名为.py 的文本文件。

censuspopdata.xlsx 电子表格中只有一张表，名为'Population by Census Tract'。每
一行都保存了一个普查区的数据。列分别是普查区的编号（A） ，州的简称（B） ，县
的名称（C） ，普查区的人口（D） 。 
'''

# •  用 openpyxl 模块打开 Excel 文档并读取单元格。
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sh = wb['Population by Census Tract']
countyData = {}

# •  计算所有普查区和人口数据，将它保存到一个数据结构中。
'''
{'AK': {'Aleutians East': {'pop': 3141, 'tracts': 1}, 
        'Aleutians West': {'pop': 5561, 'tracts': 2}, 
        'Anchorage': {'pop': 291826, 'tracts': 55}, 
        'Bethel': {'pop': 17013, 'tracts': 3}, 
        'Bristol Bay': {'pop': 997, 'tracts': 1}, 
'''
for r in range(2,sh.max_row+1):
    # 州 简称
    State = sh['B' + str(r)].value
    # 县 名称
    County = sh['C' + str(r)].value
    # 普查区人口
    POP = sh['D' + str(r)].value
    # 设置州的默认值 setdefault 没有返回默认值空字典 如果键已经存在，setdefault()不会做任何事情
    countyData.setdefault(State,{})
    countyData[State].setdefault(County,{'tracts':0,'pop':0})
    countyData[State][County]['tracts'] += 1
    countyData[State][County]['pop'] += int(POP)
print(countyData)

# •  利用 pprint 模块，将该数据结构写入一个扩展名为.py 的文本文件。

with open('census2010.py','w',encoding='utf-8') as f:
    f.write('allData = ' + pprint.pformat(countyData))
print('写入文件完成')