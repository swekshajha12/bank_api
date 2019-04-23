import psycopg2
DATABASE_URL = "postgres://cerofkbynglilr:2b7fbe4f62f1a6a37b9f1d4dad5acf495e226edd06fa169828e17009b89e0bb8@ec2-54-221-236-144.compute-1.amazonaws.com:5432/dacmbcb97s0j9e"
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur=conn.cursor()


def get_details_using_ifsc(ifsc):

	cur.execute("select * from branches_small where ifsc= '%s' "%ifsc)
	return cur.fetchall()


def get_details_using_bank_name_city(city,name):
	
	cur.execute("""select * from branches_small where city='%s' and bank_id in 
				(select id from banks where name= '%s' )"""%(name,city))
	
	return cur.fetchall()



# print(get_details_using_bank_name_city('MUMBAI','ABHYUDAYA COOPERATIVE BANK LIMITED'))

