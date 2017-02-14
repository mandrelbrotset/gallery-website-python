import mysql.connector

config = {
        'user':'database_user',
        'password':'password',
        'host':'ip_address_of_database',
        'port':'port',
        'database':'name_of_database'
        }

def insert(name,tags,image_link):
	db = mysql.connector.connect(**config)
	cursor = db.cursor()

	fields = ("INSERT INTO image_data"
              "(name, tags, image_link)"
              "VALUES(%s,%s,%s)")
	data = (name, tags, image_link)
	cursor.execute(fields, data)
	db.commit()
	cursor.close()
	db.close()
	type(name)
	print("[INFO] Success!!!")
	print("[INFO] ")
	print("[INFO] Name -------- : %s" %name)
	print("[INFO] Tag(s) ------ : %s" %tags)
	print("[INFO] Image Link -- : %s" %image_link)
	
def all():
	db = mysql.connector.connect(**config)
	cursor = db.cursor()

	query = "SELECT * FROM image_data"
	cursor.execute(query)

	rows = cursor.fetchall()
	return rows

def query(tags):
	db = mysql.connector.connect(**config)
	cursor = db.cursor()

	query = "SELECT * FROM image_data WHERE tags = '%s'"%(tags)
	cursor.execute(query)

	rows = cursor.fetchall()
	return rows

