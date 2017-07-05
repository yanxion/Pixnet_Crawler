from pyquery import PyQuery as pq

def Blog_Meta_Crawler(Web_url):
    Data = []
    res = pq(Web_url, encoding="utf-8")

    Blog_Domain = Web_url[Web_url.find('//')+2:Web_url.find('/',Web_url.find('//')+2)][Web_url[7:Web_url.find('/',Web_url.find('//')+2)].find('.')+1:]

    Blog_Account = Web_url[Web_url.find('//')+2:Web_url.find('/',Web_url.find('//')+2)][:Web_url[7:Web_url.find('/',Web_url.find('//')+2)].find('.')]

    Blog_Name =  res('div#banner').find('a').eq(0).text()

    Blog_Url = Web_url[:Web_url.find('pixnet.net/blog/')+16]


    Data.append(Blog_Domain)
    Data.append(Blog_Account)
    Data.append(Blog_Name)
    Data.append(Blog_Url)

    #Data = (Blog_Domain,Blog_Account,Blog_Name, Blog_Url)
    return Data
    #results = cursor.fetchall()

    #print results

