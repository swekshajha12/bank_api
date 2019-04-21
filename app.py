#!/usr/bin/env python
from flask import Flask,request
# from flask.ext.sqlalchemy import SQLAlchemy

# from flask.ext.heroku import Heroku
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
# heroku = Heroku(app)
# db = SQLAlchemy(app)

# from fetch_results import get_details_using_ifsc,get_details_using_bank_name_city
from fetch_res_postgresql import get_details_using_ifsc,get_details_using_bank_name_city




@app.route('/ifsc',methods=["POST"])
def hello_world():

	if request.method=="POST":
		try:

			data=request.get_json()
			print(data)

			ifsc=data['ifsc']
			ans=get_details_using_ifsc(ifsc)
			return str(ans)

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
			return str(ans)

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
