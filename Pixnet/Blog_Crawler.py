# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq
from datetime import datetime

from Pixnet import Blog_Content
from Pixnet import Blog_Meta
from Pixnet import Blog_Rank_List_url
from Pixnet import Pixnet_Type
from Pixnet import Blog_Author_List_url

import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect("localhost", "user", "user", "blog_crawler", charset='utf8')
    cursor = db.cursor()
    Insert_Meta = ("INSERT INTO blog_meta (blog_domain, blog_account, blog_name, blog_url) VALUES (%s, %s, %s, %s)")
    Insert_Content = ("INSERT INTO blog_content (`blog_domain`,`blog_account`,`blog_url`,`blog_name`,`blog_title`,`blog_type`,`blog_time`,`blog_crawltime`,`blog_content`,`blog_author`,`blog_url_sha` ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,SHA(%s))")
    Select_Content_repeat = ("SELECT blog_url_sha FROM blog_content where blog_url_sha = SHA(%s)")
    Select_meta_repeat = ("SELECT blog_url FROM blog_meta where blog_url = (%s)")

    #Web_url = "http://kusumia.pixnet.net/blog/post/252704605"
    #Web_url = "http://aerirabbit.pixnet.net/blog/post/457614977-the-chainsmokers-&-coldplay---something-just-like-this-%E4%B8%AD"
    #Pixnet.Blog_Content.Blog_Content_Crawler(Web_url)


    for i in Pixnet_Type.Pixnet_Type_url_Crawler("https://www.pixnet.net/blog"):
        for j in Blog_Rank_List_url.Blog_Type_List_Url(i):
            #meta

            print "Try Crawl Meta " + j + "... ",
            try:
                Data = Blog_Meta.Blog_Meta_Crawler(j)

                cursor.execute(Select_meta_repeat, [Data[3]])
                if cursor.fetchall():
                    print "has value."
                else:
                    try:
                        cursor.execute(Insert_Meta, Data)
                        db.commit()
                        print "done."
                    except:
                        print "error."
            except:
                print "error."

            #content
            print "Try Crawl Content " + j + "... ",
            try:
                Data = Blog_Content.Blog_Content_Crawler(j)

                cursor.execute(Select_Content_repeat, [Data[2]])

                if cursor.fetchall():
                    print "has value."
                else:
                    try:
                        cursor.execute(Insert_Content, Data)
                        db.commit()
                        print "done."
                    except:
                        print "error."
            except:
                print "error."


    """
    sql = "SELECT blog_url FROM blog_meta;"
    cursor.execute(sql)
    for i in cursor.fetchall():
        for j in Blog_Author_List_url.Blog_Author_List_Url(i[0]):
            try:
                print "Try Crawl Content " + j + "... ",
                Data = Blog_Content.Blog_Content_Crawler(j)
                cursor.execute(Select_Content_repeat, [Data[2]])
                if cursor.fetchall():
                    print "has value."
                else:
                    try:
                        cursor.execute(Insert_Content, Data)
                        db.commit()
                        print "done."
                    except:
                        print "error."

            except:
                print "error."



    """
    """
    Web_url = "http://smilejean.pixnet.net/blog/post/9860618"
    print "!!!!!!1"
    try:
        Data = Blog_Meta.Blog_Meta_Crawler(Web_url)
        print Data
    except:
        raise Exception
    """
    #cursor.execute(Insert_Content, Data)
    #db.commit()

    #Data = Pixnet.Blog_Meta.Blog_Meta_Crawler(Web_url)



    db.close()
