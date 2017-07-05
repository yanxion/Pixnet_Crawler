# -*- coding: utf-8 -*-

import MySQLdb

db = MySQLdb.connect("localhost","user","user","blog_crawler",charset='utf8')

cursor = db.cursor()

insert = ("INSERT INTO blog_meta (blog_domain, blog_account, blog_name, blog_url) VALUES (%s, %s, %s, %s)")
data = ('5', '6', '7', '8')

cursor.execute(insert, data)



#sql = "SELECT SHA('123');"
#sql = "INSERT INTO blog_meta VALUES('5','6','7','8');"
#sql = "SELECT blog_url FROM blog_meta;"


#cursor.execute(sql)

#result = cursor.fetchall()
#for record in result:
    #print record[0]
    
db.commit()
db.close()
