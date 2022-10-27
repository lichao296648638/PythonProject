import requests
import pprint
import csv

# 本地文件准备
f = open('谈小娱北京数据.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['店铺名称',
                              '店铺评分',
                              '店铺类型',
                              '评论人数',
                              '人均消费',
                              '经度',
                              '纬度',
                              '店铺详情页'])
csv_writer.writeheader()
for page in range(0, 321, 32):
    # 请求阶段
    url = 'https://apimobile.meituan.com/group/v4/poi/pcsearch/1'
    mParams = {
        'uuid': '5b33b41c073740b9b2bf.1665721008.1.0.0',
        'userid': '66496279',
        'limit': '32',
        'offset': '64',
        'cateId': '-1',
        'q': '谈小娱',
        'token': 'PJ1bqTkC7YcrgVayCiO3E5kcnf4AAAAAjxQAALXUjGsOaXo9tCwd0VHXamlksaEhaY7VfzA5vDyUw9zMeuzPzZ1dSYy9OOZkoLlT2g'
    }

    mHeaders = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'Referer': 'https://bj.meituan.com/'
    }
    response = requests.get(url, params=mParams, headers=mHeaders)

    # 解析数据并写入
    searchResult = response.json()['data']['searchResult']
    for index in searchResult:
        shop_id = index['id']
        shop_url = f'https://www.meituan.com/yundongjianshen/{shop_id}/'
        mDic = {
            '店铺名称': index['title'],
            '店铺评分': index['avgscore'],
            '店铺类型': index['backCateName'],
            '评论人数': index['comments'],
            '人均消费': index['avgprice'],
            '经度': index['longitude'],
            '纬度': index['latitude'],
            '店铺详情页': shop_url
        }
        csv_writer.writerow(mDic)
        pprint(mDic)

