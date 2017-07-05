from pyquery import PyQuery as pq


def Blog_List_url_Crawler(Web_url):
    url = []
    res = pq(Web_url, encoding="utf-8")

    if (Web_url[len(Web_url)-2:] == "/1"):
        Blog_List_Name = res('div.featured').find('h3').text()
        Blog_List_Url = res('div.featured').find('h3').find('a').attr('href')
        url.append(Blog_List_Url)
        #print "1",Blog_List_Url
    for i in range(0, res('ol.article-list').find('li').length, +1):
        if (res('ol.article-list').find('li').eq(i).find('h3').text() == ""):
            print "!!!!"
            break
        Blog_List_Name = res('ol.article-list').find('li').eq(i).find('h3').text()
        Blog_List_Url = res('ol.article-list').find('li').eq(i).find('h3').find('a').attr('href')
        url.append(Blog_List_Url)
        #print i,Blog_List_Url
    return url

def Blog_Type_List_Url(Web_url):
    cnt = 0
    url_Data = []

    if Web_url.count('/') == 6:
        Web_url += "/hot/"
    elif Web_url.count('/') == 7:
        while (Web_url.count('/') > 6):
            Web_url = Web_url[:len(Web_url) - 1]
        Web_url += "/hot/"
    elif  Web_url.count('/') == 8:
        while(1):
            if(Web_url[len(Web_url)-1:] == '/'):
                break
            else:
                Web_url = Web_url[:len(Web_url)-1]

    #Web_url[0:len(Web_url)-1]
    while(1):
        cnt += 1
        print Web_url + str(cnt)
        Data =  Blog_List_url_Crawler(Web_url + str(cnt))
        if Data == [] :
            return url_Data
        else:
            url_Data.extend(Data)

#print Blog_Type_List_Url("https://www.pixnet.net/blog/articles/category/19/hot/1")