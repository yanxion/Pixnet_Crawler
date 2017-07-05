from pyquery import PyQuery as pq

def Blog_Author_List_Crawler(Web_url):
    url = []
    res = pq(Web_url, encoding="utf-8")

    #test =  res('div.article').find('li.title').find('a').eq(1).text()

    #print res('div.article').find('li.title').find('a').length
    for i in range(0,res('div.article').find('li.title').find('a').length,+1):
        Data  = res('div.article').find('li.title').find('h2').find('a').eq(i).attr('href')
        #print Data
        url.append(Data)
    return url

def Blog_Author_List_Url(Web_url):
    cnt = 0
    url_Data = []
    while (1):
        cnt += 1
        print Web_url + str(cnt)
        Data = Blog_Author_List_Crawler(Web_url + str(cnt))
        if Data == []:
            return url_Data
        else:
            url_Data.extend(Data)


#print Blog_Author_List_Url("http://a24195.pixnet.net/blog/")
#print Blog_Author_List_Url("http://sabellawu.pixnet.net/blog/")

