#coding=utf-8
import os
import sys

sys.path.append(os.path.join(os.path.split(os.path.abspath(__file__))[0], '..'))

import json
import tornado.web
import numpy as np
from common import errors


# curl --request POST --url http://localhost:8030/test --header 'content-type: application/json'
# --data '{"model_names": ['spkr0001.mdl', 'spkr0002.mdl'],
#           "model_path": "http://huge.yiwei.callcenter.corp/models/",
#           "wav_path": "http://huge.yiwei.callcenter.corp/register/"
#           "wav_names": ["201801240004.wav", "201801240005.wav", "201801240006.wav"]}'
# response: {"result": "success",
#            "data": "{'201801240004.wav': {'spkr0001.mdl': 0.80, 'spkr0002.mdl': 0.50},
#                      '201801240005.wav': {'spkr0001.mdl': 0.20, 'spkr0002.mdl': 0.40},
#                      '201801240006.wav': {'spkr0001.mdl': 0.40, 'spkr0002.mdl': 0.40}}"}
#        or {'result': "error", 'data': 'error_msg'}


def test_scores(model_path, model_names, wav_path, wav_names):
    score_map = {}
    for i in wav_names:
        scores = {}
        for m in model_names:
            scores[m] = round(np.random.rand(), 2)
        score_map[i] = scores
    return score_map


class TestHandler(tornado.web.RequestHandler):
    def post(self):
        try:
            data = json.loads(bytes.decode(self.request.body))
            model_names = data['model_names']
            model_path = data['model_path']
            wav_names = data['model_names']
            wav_path = data['wav_path']
        except:
            print(data)
            self.write_error(errors.HTTP_BAD_REQUEST, msg='post body format error')
            return

        ret = test_scores(model_path, model_names, wav_path, wav_names)

        resp = json.dumps({
            "result": "success",
            "data": ret
        })
        self.write(resp)

    def write_error(self, status_code, **kwargs):
        resp = json.dumps({
            "result": "error",
            "message": kwargs['msg']
        })
        self.write(resp)


if __name__ == '__main__':

    model_names = ['spkr0001.mdl', 'spkr0002.mdl']
    model_path = "http://huge.yiwei.callcenter.corp/models/"
    wav_path = "http://huge.yiwei.callcenter.corp/register/"
    wav_names = ["201801240004.wav", "201801240005.wav", "201801240006.wav"]

    ret = test_scores(model_path, model_names, wav_path, wav_names)
    print(ret)