import json
from flask import Response

from common.common_config import CODES



def response_json(res=None):
    return {'result': res, 'data': None} if type(res) == int else {'result': CODES['SUCCESS'], 'data': res}

def make_response(data=None):
    print 'res : ' + json.dumps(response_json(data))
    return Response(json.dumps(response_json(data)), mimetype='application/json')
