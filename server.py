import json, sys
from flask import request

from common.flask import app
from common.common_config import CODES
from common.database.models import User
from sqlalchemy import or_
from common.database.create import create_all

import common.helper

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/update')
def update():
    create_all()
    return 'create_all function called'

@app.route('/withgamecenter', methods=['POST'])
def withgamecenter():
    #try:

	req = request.json

        if req['gamecenterId'] != '':
	    user = User.query.filter(or_(User.device_id==req['deviceId'], User.social_token==req['gamecenterId'])).first()
	else:
	    user = User.query.filter_by(device_id=req['deviceId']).first()
	if not user:

	    user = User()
	    user.device_id = req['deviceId']
	    user.social_token = req['gamecenterId']
	    user.stage_open = 1
	    user.stage_clear = 1
	    user.hint = 5

	    app.db.session.add(user)
	    app.db.session.commit()

	    result = {

		'user':user.to_dict()
	    }

	return common.helper.make_response(result)

    #except:
    #    print "Unexpected error:", sys.exc_info()[0]
    #    return common.helper.make_response(CODES['FAILURE'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)


