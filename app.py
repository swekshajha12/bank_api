#!/usr/bin/env python
from flask import Flask,request,jsonify
from fetch_res_postgresql import get_details_using_ifsc,get_details_using_bank_name_city
app = Flask(__name__)

def check_if_get_post(url,meth):
	if url =='details':

		if meth=="POST":
			data=request.get_json()
			return data['bank_name'],data['city']
		else:
			return request.headers['bank_name'],request.headers['city']

	elif url=='ifsc':
		
		if meth=="POST":
			data=request.get_json()
			return data['ifsc']
		else:
			return request.headers['ifsc']
				


@app.route('/ifsc',methods=["GET","POST"])
def ifsc():

	
	try:
		
		
		ifsc=check_if_get_post('ifsc',request.method)
		li=["ifsc","bank_id","branch","address","city","dist","state"]
		dc={}
		ans=get_details_using_ifsc(ifsc)
		# print(type(ans))

		for i,j in enumerate(ans[0]):
			dc[li[i]]=j
		return jsonify(dc)

	except Exception as e:
		print(e)
		
		return 'No success'	



@app.route('/details',methods=["GET","POST"])
def details():

	
	try:

		
		# print(request.headers)
		# name=request.headers['bank_name']
		# city=request.headers['city']
		name,city=check_if_get_post('details',request.method)
		ans=get_details_using_bank_name_city(name,city)

		li=["ifsc","bank_id","branch","address","city","dist","state"]

		dc={}

		for i,j in enumerate(ans):
			dc[i]={}

			for no,row_elements in enumerate(j):
				dc[i][li[no]]=row_elements
	

		# print(type(ans))
		return jsonify(dc)

	except Exception as e:
		print(e)
	
		return 'No success'	


if __name__ == '__main__':
	app.run(debug=True,port=8000)

'''

{
"bank_name":"ABHYUDAYA COOPERATIVE BANK LIMITED",
"city":"MUMBAI"
}


{
"ifsc":"ABHY0065046"
}

'''	