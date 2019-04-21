#!/usr/bin/env python
from flask import Flask,request,jsonify

from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

from fetch_res_postgresql import get_details_using_ifsc,get_details_using_bank_name_city

@app.route('/ifsc',methods=["POST"])
def hello_world():

	if request.method=="POST":
		try:

			data=request.get_json()
			print(data)

			ifsc=data['ifsc']
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


@app.route('/details',methods=["POST"])
def hello():

	if request.method=="POST":
		try:

			data=request.get_json()
			# print(data)

			name=data['bank_name']
			city=data['city']
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
