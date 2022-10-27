import parsel
import random
import requests
from openpyxl import Workbook
import time
from fake_useragent import UserAgent

# 随机UA
ua = UserAgent()

# 创建一个 workbook
wb = Workbook()
# 获取被激活的 worksheet
ws = wb.active
# 设置单元格内容
ws['A1'] = '小区名字'
ws['B1'] = '所属分区'
ws['C1'] = '建成时间'
ws['D1'] = '房价m²'
ws['E1'] = '户数'
ws['F1'] = '物业公司'
ws['G1'] = '联系电话'

# # 代理池
# f_ip = open(r'E:\PythonProject\代理\ok_ip.txt', 'r')
# ip_list = []
# for ip in f_ip.readlines():
#     ip_list.append(ip)


# 爬取安居客
def ajk_data():
    # 烟台安居客二手房列表
    ajk_list_url = 'https://yt.anjuke.com/community/p1/'

    # 安居客UA伪装
    ajk_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'Cookie': 'aQQ_ajkguid=B917995C-483E-3BD4-25FD-8194F1544496; id58=CrIcnGL+UmC9m6lcE8eVAg==; 58tj_uuid=5010be80-a063-45c6-96c0-9205343c93cb; ajk-appVersion=; seo_source_type=1; xxzl_cid=a41456d935fb432986a616c82885f820; xzuid=1550c86c-4637-4fad-ab25-a147597c380b; fzq_h=5587d114d91c2e79447e1a598c428069_1666805932291_0ba6302425144b7a88f9a2e33d80d69e_2353783494; als=0; _ga=GA1.2.851383827.1666819292; _gid=GA1.2.1037953870.1666819292; sessid=AE8BB64A-92C1-1935-2943-5D48C3024594; twe=2; ctid=47; obtain_by=2; new_session=1; init_refer=; new_uv=7; fzq_js_anjuke_xiaoqu_pc=e35d3f9020a7f6771a8ec017c821e185_1666892127040_23; ajk_member_verify=QfrsoBNLIjXvC8uI8uMcHZFB2fKTJwF+rPQ8u3YPrFE=; ajk_member_verify2=MjU4NTcwMjA1fEVwRGpRelZ8MQ==; ajkAuthTicket=TT=80c31316b82816d4925fa9c7ff60fa1c&TS=1666892127348&PBODY=QfpREvgl1tUjF4nmx763zBIzkgtxyf0fzP0_AkZWV1zgP4OadMBhJKX5kt1i8XDclyoufP0lLzZwW8Q-lT4oocHGmtNAZglQLzjJ0eNBNwhvYXkHg7vVjGBrFgQMgx9bu49lhvM-frbblPgZND1DunXnE0DTktT0bNFPT39uY9o&VER=2&CUID=GDzCNgmydFE6pPc8h58IvHKyO1Hvr8W-; xxzl_cid=a41456d935fb432986a616c82885f820; xxzl_deviceid=F1E7W4juTbq4Kn6vM++iwgJPl6a6eQbBFOcbJFlSpQb/1EQFM1EKXGTz/lIo1y4F'
    }

    # 企业列表UA伪装
    company_list_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'Cookie': 'BIDUPSID=16014FA3CCB976F243A46BEF9A133856; PSTM=1624476031; __yjs_duid=1_e1e2e8ec199b66db1484deac8fd6f0a51624547332369; log_guid=86302942924849f46cb3f885326fe844; BAIDUID=67EB5758B603FE732F773C90EDF20380:FG=1; MCITY=-326:; _j47_ka8_=57; BDUSS=GF5ZGxzR0dReUM1eUk1eUg2bX5YSVFNN2dJREF3UG9vUGJpcTc5fk16WEkwMzFqRVFBQUFBJCQAAAAAAAAAAAEAAACpRKsHxL7Nt8vAxL7NtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMhGVmPIRlZjZ; BDUSS_BFESS=GF5ZGxzR0dReUM1eUk1eUg2bX5YSVFNN2dJREF3UG9vUGJpcTc5fk16WEkwMzFqRVFBQUFBJCQAAAAAAAAAAAEAAACpRKsHxL7Nt8vAxL7NtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMhGVmPIRlZjZ; BDPPN=b17d62b0cbe0b97010f027d9dfdc8bb9; _t4z_qc8_=xlTM-TogKuTwcMhwBtN*FEmMqbF6LQ3bQwmd; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_ad52b306e1ae4557f5d3534cce8f8bbf=1666597899,1666827899,1666892934; _fb537_=xlTM-TogKuTwS6l*wsc*V-OJ8fC0shyYFylCP1zgNjHP3jZEngU1y2Umd; _s53_d91_=b905d1f221e72c9fbe6c5b75c71823024829ea664362d3b9a8b7f6014dacce7f7a49de59bfc92927f476223e34a94a5bd600cb0be4b655fd8e960acfdf21f9cf7c49540359ea55ff9d4eb20912275512699b36070805f1265bc69f4a3f20ba52f29f2880ca8c3482476db61f6f75a50a7537ce0c9220245d1cc99d4e719410c1205801b3579618ec7212d83061a90654d1eb142391411a01aee648b073d5154469c84a8d06250b3102aead6c670a2db094d17b3e07ee2f62cb20407a616693178efed88fc67582b2c89d11ce345923376d4781035051597bf0360a4e7836ff20; _y18_s21_=bff9bfc8; ab_sr=1.0.1_YjY4M2I3OWQxZDEzMjhmM2NkOTk1MzU0ODVhNGU5ZWY4NTIzOGI2OGE2ZDkxOTlhYTkzMzM3NGJiOTNhYmE2YmI5YmU2NjAzZTdmNmRiYTljZjNiODY5ZDFhNTVmYjIwZGQ0MWIzMWZmNTBlZGNkYjIxMmQ1MDgwODU1NzNlNzY4MjMyMDJkMzM2ZmQxMjEyN2YwNGRhOWY4OTViNjVmMGFkZjcwYTRkODk4MGQ1OThkZmZlZjVjYzQxNWVkMGVj; H_PS_PSSID=37543_36557_37515_37352_37584_36885_34813_37627_36806_36789_37532_37499_37581_26350_22158; log_first_time=1666898182573; BAIDUID_BFESS=67EB5758B603FE732F773C90EDF20380:FG=1; log_last_time=1666898488493; ab166689720=22a150cb243bbd9d2937e847a558395216668984900e0; Hm_lpvt_ad52b306e1ae4557f5d3534cce8f8bbf=1666898490; RT="z=1&dm=baidu.com&si=ce36d77e-176e-4601-9620-65c672c64f72&ss=l9rd0ia7&sl=t&tt=kgd&bcn=https://fclog.baidu.com/log/weirwood?type=perf&ul=3b4g8"'
    }

    # 爱企查详情UA伪装
    aqc_item_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'Cookie': 'BIDUPSID=16014FA3CCB976F243A46BEF9A133856; PSTM=1624476031; __yjs_duid=1_e1e2e8ec199b66db1484deac8fd6f0a51624547332369; log_guid=86302942924849f46cb3f885326fe844; BAIDUID=67EB5758B603FE732F773C90EDF20380:FG=1; MCITY=-326:; _j47_ka8_=57; BDUSS=GF5ZGxzR0dReUM1eUk1eUg2bX5YSVFNN2dJREF3UG9vUGJpcTc5fk16WEkwMzFqRVFBQUFBJCQAAAAAAAAAAAEAAACpRKsHxL7Nt8vAxL7NtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMhGVmPIRlZjZ; BDUSS_BFESS=GF5ZGxzR0dReUM1eUk1eUg2bX5YSVFNN2dJREF3UG9vUGJpcTc5fk16WEkwMzFqRVFBQUFBJCQAAAAAAAAAAAEAAACpRKsHxL7Nt8vAxL7NtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMhGVmPIRlZjZ; BDPPN=b17d62b0cbe0b97010f027d9dfdc8bb9; _t4z_qc8_=xlTM-TogKuTwcMhwBtN*FEmMqbF6LQ3bQwmd; BA_HECTOR=252084240lak00002k817m011hlkj031b; delPer=0; PSINO=5; BAIDUID_BFESS=67EB5758B603FE732F773C90EDF20380:FG=1; ZFY=tVEdSIrSdGzgCNqr:AAvPQb27TqyETFI:AcXmYepmUMrs:C; BDRCVFR[0-iYRofrloc]=-48_i3v-l4_uhN8uvFLQhP8; ZD_ENTRY=baidu; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=37543_36557_37515_37352_37584_36885_34813_37627_36806_36789_37532_37499_37581_26350_22158; Hm_lvt_ad52b306e1ae4557f5d3534cce8f8bbf=1666597899,1666827899,1666892934; log_first_time=1666892933735; _fb537_=xlTM-TogKuTwS6l*wsc*V-OJ8fC0shyYF6VrJMTVCViIdFDbEDQZO5Ymd; ab166689000=21a150cb243bbd9d2937e847a558395216668930542e4; Hm_lpvt_ad52b306e1ae4557f5d3534cce8f8bbf=1666893055; ab_sr=1.0.1_ZjcxNzZhZTJkMTE3ZDA1MGEwOTA3NDliMjE1ZTI1ZTUwNGViNGEzNmMzYWE2NDU3MDRjZTJhM2EzNThjNDY1N2YwM2MyZTc1NThkM2Y2NGY3OGYxYmIwY2ViYTc0YzJiYjQ2YTJlMjc5NTk4MTEwN2ViOGQ0NDlhNWY0ZDFjY2EwZGRjODJlY2I2Yzg0NjRmYTU2ZjZhYjRkMDRkNTBlNA==; _s53_d91_=b905d1f221e72c9fbe6c5b75c71823024829ea664362d3b9a8b7f6014dacce7f7a49de59bfc92927f476223e34a94a5bd600cb0be4b655fd8e960acfdf21f9cf7c49540359ea55ff9d4eb20912275512699b36070805f1265bc69f4a3f20ba52f29f2880ca8c3482476db61f6f75a50a7537ce0c9220245d1cc99d4e719410c1205801b3579618ec7212d83061a90654d1eb142391411a01aee648b073d5154469c84a8d06250b3102aead6c670a2db0e5cd0dc5c026aa9e5eb57a69671fb8f7de9456f9573cfbb9bd1a5064ce657e476e3e52925c2947fc6b8d0ca67787e144; _y18_s21_=57ecda3d; RT="z=1&dm=baidu.com&si=ce36d77e-176e-4601-9620-65c672c64f72&ss=l9rd0ia7&sl=f&tt=8uw&bcn=https://fclog.baidu.com/log/weirwood?type=perf&ld=3pt3"; log_last_time=1666893110087'
    }

    # 发送请求
    response = requests.get(ajk_list_url, headers=ajk_headers)

    # 获取数据
    ajk_list_html = response.text

    print('--------------------------列表页爬取完成--------------------------------------------')

    # 解析数据 .li-row 的列表项
    list_selector = parsel.Selector(text=ajk_list_html)
    divs = list_selector.css('.li-row')

    # 把div中的详情内容进行提取
    for div in divs:
        # 安居客详情页链接
        item_url = div.css('::attr(href)').get()

        # 抓取详情页信息
        ajk_item_html = requests.get(url=item_url, headers=ajk_headers).text

        # 解析详情页数据
        item_selector = parsel.Selector(text=ajk_item_html)

        # 户数
        house_num = item_selector.css('.value.value_4::text').get().strip()

        # 物业公司
        property = item_selector.css('.info-list .column-1:nth-child(17) .value::text').get().strip()

        # 查企业列表页链接
        company_list_url = 'https://aiqicha.baidu.com/s'

        # 爱企查请求参数
        company_params = {
            'q': property,
            't': 0
        }


        # 请求企业列表数据
        company_list_html = requests.get(url=company_list_url, headers=company_list_headers, params=company_params).text
        with open('test.html', "w", encoding="utf-16") as f:
            f.write(company_list_html)
        print('---------------------企业表页--------------------')
        # 解析爱企查列表页
        company_list_selector = parsel.Selector(text=company_list_html)

        # # 拿到爱企查详情页链接
        # aqc_item_url = company_list_selector.css('.company-list::text').get()
        #
        # print(aqc_item_url)
        #
        # # 请求爱企查详情数据
        #
        # aqc_item_html = requests.get(url=aqc_item_url, headers=aqc_item_headers, params=company_params).text
        #
        # # 解析爱企查详情页
        # aqc_item_selector = parsel.Selector(text=aqc_item_html)
        #
        # # 物业电话
        # property_tel = aqc_item_selector.css('.copy-box>span::text').get()

        # 物业电话
        property_tel = company_list_selector.css('.index_value__Pl0Nh>span::text').get()

        # ---------写入单行数据-----------
        # 小区名字
        ws.append([div.css('.nowrap-min.li-community-title::text').get(),
                   # 所属分区
                   div.css('.split-line+span::text').get(),
                   # 建成时间
                   div.css('.year::text').get(),
                   # 房价
                   div.css('.community-price>strong::text').get(),
                   # 户数
                   house_num,
                   # 物业公司
                   property,
                   # 物业电话
                   property_tel
                   ])
        wb.save("test.xlsx")
        random_sleep(3, 1)
    print('------------------------------数据写入完成----------------------------------------')


ajk_data()


def random_sleep(mu=1, sigma=0.4):
    '''正态分布随机睡眠

    :param mu: 平均值

    :param sigma: 标准差，决定波动范围

    '''

    secs = random.normalvariate(mu, sigma)

    if secs <= 0:
        secs = mu  # 太小则重置为平均值

        time.sleep(secs)
