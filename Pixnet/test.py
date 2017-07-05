import MySQLdb


db = MySQLdb.connect("localhost", "user", "user", "blog_crawler", charset='utf8')
cursor = db.cursor()

sql = "SELECT blog_url FROM blog_meta;"
#data = ["http://sabellawu.pixnet.net/blog/post/455560445"]

cursor.execute(sql)

result = cursor.fetchall()
#print result

for record in result:
    print record[0]

