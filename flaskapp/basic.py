from flask import Flask, request,json


app = Flask(__name__)
# api = Api(app)

@app.route('/hello')
def api_hello():
	return "helloworld"



	
if __name__ == '__main__':
	app.run()