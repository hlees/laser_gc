import json
from flask import Flask

from common.common_config import CODES

app = Flask(__name__)

@app.route('/')
def hello_world():
    print 'what the fuck!'
    return 'Hello World!'

@app.route('/withgamecenter', methods=['POST'])
def withgamecenter():
    try:

        app.logger.debug("request data")
	print request.data
        _req = json.loads(request.data)
	print "json.loads(request.data)"
	print _req

	return common.helper.make_response(CODES['SUCCESS'])

    except:
        print("Unexpected error:", sys.exc_info()[0])
        return common.helper.make_response(CODES['FAILURE'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


