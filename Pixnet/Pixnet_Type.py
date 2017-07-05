from pyquery import PyQuery as pq

def Pixnet_Type_url_Crawler(Web_url):
    Data = []
    res = pq(Web_url, encoding="utf-8")

    Type_Name = res('ul#navigation').find('ul').find('a').text()

    cnt = 0
    for i in Type_Name.split(' '):
        Type_Url = res('ul#navigation').find('ul').find('a').eq(cnt).attr('href')
        Data.append("https://www.pixnet.net" + Type_Url)
        cnt += 1

    return Data
