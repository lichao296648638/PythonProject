# -*- coding = utf-8 -*-
# @Time : 2021/1/23 16:08
# @Author : Ruler_Madman
# @File : demo1.py
# @Software : PyCharm
"""
基于天眼查网站https://www.tianyancha.com/
根据公司全称查询详细公司介绍的链接和联系方式
"""

import requests
from lxml import etree
heads = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Cookie": "TYCID=7b4fd470377611eba3d419c6d13dcd58; ssuid=5809544952; _ga=GA1.2.486119447.1607226759; tyc-user-phone=%255B%252219917221571%2522%255D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22176362e1356102-00a227b2f6d89f-c791039-1327104-176362e135c130%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22176362e1356102-00a227b2f6d89f-c791039-1327104-176362e135c130%22%7D; tyc-user-info={%22claimEditPoint%22:%220%22%2C%22vipToMonth%22:%22false%22%2C%22explainPoint%22:%220%22%2C%22personalClaimType%22:%22none%22%2C%22integrity%22:%2210%25%22%2C%22state%22:%220%22%2C%22score%22:%220%22%2C%22announcementPoint%22:%220%22%2C%22messageShowRedPoint%22:%220%22%2C%22bidSubscribe%22:%22-1%22%2C%22vipManager%22:%220%22%2C%22onum%22:%220%22%2C%22monitorUnreadCount%22:%220%22%2C%22discussCommendCount%22:%220%22%2C%22showPost%22:null%2C%22messageBubbleCount%22:%220%22%2C%22claimPoint%22:%220%22%2C%22token%22:%22eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxOTkxNzIyMTU3MSIsImlhdCI6MTYwNzI0MDQ4OSwiZXhwIjoxNjM4Nzc2NDg5fQ.H_nWUC_MsH8WfVzI_Yi0NOlOIX52i2hNVC8gDnrlCcLAEi0NgMLYEU0n7J5qTD6nVBsbIf_7qlikOcAAdOlKSA%22%2C%22schoolAuthStatus%22:%222%22%2C%22userId%22:%22221996029%22%2C%22scoreUnit%22:%22%22%2C%22redPoint%22:%220%22%2C%22myTidings%22:%220%22%2C%22companyAuthStatus%22:%222%22%2C%22originalScore%22:%220%22%2C%22myAnswerCount%22:%220%22%2C%22myQuestionCount%22:%220%22%2C%22signUp%22:%220%22%2C%22privateMessagePointWeb%22:%220%22%2C%22nickname%22:%22%E6%9D%8E%C2%B7%E5%A4%8F%E6%99%AE%22%2C%22privateMessagePoint%22:%220%22%2C%22bossStatus%22:%222%22%2C%22isClaim%22:%220%22%2C%22yellowDiamondEndTime%22:%220%22%2C%22yellowDiamondStatus%22:%22-1%22%2C%22pleaseAnswerCount%22:%220%22%2C%22bizCardUnread%22:%220%22%2C%22vnum%22:%220%22%2C%22mobile%22:%2219917221571%22%2C%22riskManagement%22:{%22servicePhone%22:null%2C%22mobile%22:19917221571%2C%22title%22:null%2C%22currentStatus%22:null%2C%22lastStatus%22:null%2C%22quickReturn%22:false%2C%22oldVersionMessage%22:null%2C%22riskMessage%22:null}}; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxOTkxNzIyMTU3MSIsImlhdCI6MTYwNzI0MDQ4OSwiZXhwIjoxNjM4Nzc2NDg5fQ.H_nWUC_MsH8WfVzI_Yi0NOlOIX52i2hNVC8gDnrlCcLAEi0NgMLYEU0n7J5qTD6nVBsbIf_7qlikOcAAdOlKSA; tyc-user-info-save-time=1607240487082; bad_id658cce70-d9dc-11e9-96c6-833900356dc6=b03fe0f1-3869-11eb-b0ae-01f1e2a1bbb4; bad_idf0615f20-d9d7-11e9-96c6-833900356dc6=b61a4ab1-3869-11eb-b732-ddb0f20dbbb8; csrfToken=sIPMLSKVRUJNuv_r3jvdZzNt; bannerFlag=true; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1610354670,1610417438,1610801207,1611708200; _gid=GA1.2.739364670.1611708201; aliyungf_tc=2c5233d8ffea3917d132be4318e216bc69572dab6972c8ee5c359e0589abe2ce; acw_tc=781bad0e16117400398081585e07a0d2a50443a9d5f65f638116c86b8680d4; RTYCID=bd4f870d87594e0caae67d26ce7f1c4a; CT_TYCID=d61df2d27ff44458abae618c50e2e55e; cloud_token=c77a793271c9470981603fdb82f6423b; cloud_utm=caabcd147ef048559e9d0e1eadb56097; relatedHumanSearchGraphId=142260828; relatedHumanSearchGraphId.sig=2xLb5k7rjsxYHNRDEp0VkTDimteXRU1znckQn-AuPvc; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1611740122; _gat_gtag_UA_123487620_1=1; searchSessionId=1611740130.29658842",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
    }
def getgsurl(key):
    global heads
    url = "https://www.tianyancha.com/search?key=" + key
    res = requests.get(url, headers=heads).text
    res = etree.HTML(res)
    r = res.xpath("//div[@class='scroll-list']//a/@href")[0]
    rn = r.find("-c")
    with open('test.html', "w", encoding="utf-16") as f:
        f.write(res)
    gsurl = "https://www.tianyancha.com/company/" + r[rn+2:]
    return gsurl

def getgsnum(url):
    global heads
    res = requests.get(url, headers=heads).text
    res = etree.HTML(res)
    r = res.xpath("//div[@class='f0']//span")[3].text
    return r

def main():
    key = input("请输入公司全名：")
    gsurl = getgsurl(key)
    gsnum = getgsnum(gsurl)
    print("公司信息网址：", gsurl)
    print("公司联系电话：", gsnum)
    input()

if __name__ == '__main__':
    main()