from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def helloworld():
	if(request.method == 'GET'):
		data = {"data": "Endpoint is running!!!"}
		return jsonify(data)
	
@app.route('/',methods=['GET'])
def home():
	if(request.method == 'GET'):
		data = {"data": "Server is running!!!"}
		return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001)