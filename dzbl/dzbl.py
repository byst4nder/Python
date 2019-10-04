
import json
import time
import re

import requests
from lxml import etree
import xlwt
import pandas as pd


class  Dzbl():


    user_name = ''
    password = ''
    header = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Length": "0",
            "Host": "sjzx.niha.org.cn",
            "Origin": "http://sjzx.niha.org.cn",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
    }

    login_data = {
        "loginName": "DZBL450388559",
        "loginPassword": "DZBLcqszfy9174"
    }

    # 初始化
    def  __init__(self,fieldset_xpath='',table_xpath='',item_xpath='',username=None,passwd=None):

        self.fieldset_xpath = fieldset_xpath
        self.table_xpath = table_xpath
        self.item_xpath = item_xpath
        self.user_name = username
        self.password = passwd



    def Login(self,url):
        sess = requests.session()
        r = sess.post(url,headers = self.header,data=self.login_data)
        if r.status_code==200:
            print('登录成功!')
            cookie_dict = requests.utils.dict_from_cookiejar(sess.cookies)
            with open('dzbl_cookies.json', 'w', encoding='utf-8') as f:
                json.dump(cookie_dict, f)
        else:
            print('登录失败！')

    def Check_data(self,data):
        if data:
            data=data[0].split()
            return data
        else:
            return None

    def Check_title(self,data):
        if data:
            data=data[2].split()
            return data
        else:
            return None

    def Base_spider(self,url):
        # 读取cookie
        with open('dzbl_cookies.json','r') as f:
            cookie=requests.utils.cookiejar_from_dict(json.load(f))
        r = requests.get(url,headers=self.header,cookies=cookie)

        data_list = []
        if r.status_code == 200:
            rp = etree.HTML(r.text.replace('\r\n',''))
            part = self.Check_data(rp.xpath('//*[@id="maincon"]/div[1]/h2/text()'))
            for rf in rp.xpath(self.fieldset_xpath):
                title = self.Check_title(rf.xpath('.//legend/text()'))
                for rp_data in rf.xpath(self.table_xpath):
                    d = {}
                    d['part'] = part
                    d['title'] = title
                    d['id'] = self.Check_data(rp_data.xpath('.//td[@class="formfieldM"]/input[1]/@id')),
                    d['name'] = self.Check_data(rp_data.xpath('.//td[@class="formfieldM"]/input[1]/@name')),
                    d['no'] = self.Check_data(re.findall('\d{1,2}\.\d{1,2}.\d{1,2}',etree.tostring(rp_data, encoding=str))),

                    if d['no'][0]:
                        d['itern'] = self.Check_data(rp_data.xpath('.//td[2]/span/text()')),
                    else:
                        d['itern'] = self.Check_data(rp_data.xpath(self.item_xpath['itern'])),
                    if d['part'][0] == '电子病历基础' or d['part'][0] == '信息利用':
                        # d['num'] = self.Check_data(rp_data.xpath('.//td[@class="formfieldM"]/select/option[@selected]/@value')),
                        d['num'] = self.Check_data(re.findall('option\svalue="(1)"\sselected.*?option',etree.tostring(rp_data, encoding=str))),
                        # print(d['num'])

                        pass

                    else:
                        d['num'] = self.Check_data(rp_data.xpath(self.item_xpath['num'])),
                        d['unit'] = self.Check_data(rp_data.xpath(self.item_xpath['unit']))
                        pass


                    data_list.append(d)

        return data_list





def export_excel(export):
   #将字典列表转换为DataFrame
   pf = pd.DataFrame(list(export))
   #指定字段顺序
   order = ["part", "title", "id", "name", "no", "itern", "num", "unit"]
   # ["part": ["病房医师"], "title": ["一、病房医嘱处理部分"], "id": [["BASE1"]], "name": [null], "no": [null], "itern": [
   #     ["医院运行基础数据：全部出院人数:"]], "num": [["4765"]], "unit": ["人次"]]
   # order = ['road_name','bus_plate','timeline','road_type','site']
   pf = pf[order]
   #将列名替换为中文
   columns_map = {
      "part": 'part',
       "title": 'title',
       "id": 'id',
       "name": 'IDname',
       "no": '编号',
       "itern": '条目',
       "num": '数量',
       "unit": "单位"
   }
   pf.rename(columns = columns_map,inplace = True)
   #指定生成的Excel表格名称
   file_path = pd.ExcelWriter('name.xlsx')
   #替换空单元格
   pf.fillna(' ',inplace = True)
   #输出
   pf.to_excel(file_path,encoding = 'utf-8',index = False)
   #保存表格
   file_path.save()

if __name__ == "__main__":
    login_url = 'http://sjzx.niha.org.cn/Login/Index'
    d1_url_list = ['http://sjzx.niha.org.cn/Temp/Basic?subjectid=281be2fe-bfc4-4c93-88be-d4443b1c7f65&tempid=EMRT0{}&version=0.0.0.1&tempstatus=1&checkId=1'.format(i) for i in range(11,21)]
    d2_url_list = ['http://sjzx.niha.org.cn/Temp/Basic?subjectid=281be2fe-bfc4-4c93-88be-d4443b1c7f65&tempid=DT00{}&version=0.0.0.1&tempstatus=1&checkId=1&flag=view'.format(i) for i in range(1,10)]

    fieldset_xpath='//*[@id="regForm"]/fieldset'
    table_xpath = './/div/div/table/tr'
    item_xpath = {
        'no':'.//td[1]/text()',
        'itern':'.//td[2]/text()',
        'num':'.//td[@class="formfieldM"]/input[1]/@value',
        'unit':'.//td[@class="formfieldM"]/label/text()'
    }

    dzbl = Dzbl(fieldset_xpath,table_xpath,item_xpath)
    # dzbl.Login(login_url)
    for data_url in d1_url_list:
        data = dzbl.Base_spider(data_url)
        export_excel(data)
        with open('data_4.txt', 'a', encoding='utf-8') as f:
            for i in data:
                json.dump(i,f,ensure_ascii=False)
                f.write('\n')
                print(i)
        time.sleep(5)
    # for data_url in d2_url_list:
    #     data = dzbl.Base_spider(data_url)
    #     with open('data_3.txt', 'a', encoding='utf-8') as f:
    #         for i in data:
    #             json.dump(i,f,ensure_ascii=False)
    #             f.write('\n')
    #             print(i)
    #     time.sleep(5)