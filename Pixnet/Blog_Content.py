from pyquery import PyQuery as pq
from datetime import datetime


def Blog_Content_Crawler(Web_url):
    Data = []
    res = pq(Web_url, encoding="utf-8")

    Blog_Domain = Web_url[Web_url.find('//')+2:Web_url.find('/',Web_url.find('//')+2)][Web_url[7:Web_url.find('/',Web_url.find('//')+2)].find('.')+1:]

    Blog_Account = Web_url[Web_url.find('//')+2:Web_url.find('/',Web_url.find('//')+2)][:Web_url[7:Web_url.find('/',Web_url.find('//')+2)].find('.')]

    Blog_Url = Web_url

    Blog_Name =  res('div#banner').find('a').eq(0).text()

    Blog_Title = res('li.title').find('h2').find('a').text()

    Blog_Type = res('ul.refer').find('li').eq(0).find('a').text()

    Blog_Time = datetime.strptime(res('li.publish').find('.year').text()[2:] + '-' + res('li.publish').find('.month').text() + '-' + res('li.publish').find('.date').text() + ' ' + res('li.publish').find('.time').text(), "%y-%b-%d %H:%M")
    """
    print res('li.publish').find('.year').text()[2:]

    print res('li.publish').find('.month').text()

    print res('li.publish').find('.date').text()

    print res('li.publish').find('.time').text()

    print "!!!!"
    """
    Blog_Crawler_Time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    Blog_Content = res('div.article-content-inner').find('p').text()

    Blog_Author = res('div.box-text').find('dl').find('dd').eq(0).text()

    #Blog_Url_Sha = select SHA("1123")

    Data.append(Blog_Domain)
    Data.append(Blog_Account)
    Data.append(Blog_Url)
    Data.append(Blog_Name)
    Data.append(Blog_Title)
    Data.append(Blog_Type)
    Data.append(str(Blog_Time))
    Data.append(str(Blog_Crawler_Time))
    Data.append(Blog_Content)
    Data.append(Blog_Author)
    Data.append(Blog_Url)
    #Data = (Blog_Domain,Blog_Account,Blog_Url,Blog_Name,Blog_Title,Blog_Type,Blog_Time,Blog_Crawler_Time,Blog_Content,Blog_Author,Blog_Url)

    return Data