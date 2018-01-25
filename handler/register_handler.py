#coding=utf-8
import os
import sys

sys.path.append(os.path.join(os.path.split(os.path.abspath(__file__))[0], '..'))

import json
import tornado.web
from common import errors

# api example
# curl --request POST --url http://localhost:8030/register --header 'content-type: application/json'
# --data '{"speaker_id": 0001,
#          "wav_path": "http://huge.yiwei.callcenter.corp/register/"
#          "wav_names": ["201801240001.wav", "201801240002.wav", "201801240003.wav"],
#          "model_path": "http://huge.yiwei.callcenter.corp/models/",
#          "model_name": "spkr0001.mdl"}'
# response: {"result": "success"}
#        or {'result': "error", 'data': 'error_msg'}


def register_speaker(speaker_id, wav_path, wav_names, model_path, model_name):
    print(speaker_id)
    print(wav_path)
    print(wav_names)
    print(model_path)
    print(model_name)
    return True


class RegisterHandler(tornado.web.RequestHandler):
    def post(self):
        try:
            print(self.request.body)
            data = json.loads(bytes.decode(self.request.body))
            print(data)
            speaker_id = data['speaker_id']
            wav_path = data['wav_path']
            wav_names = data['wav_names']
            model_path = data['model_path']
            model_name = data['model_name']
        except:
            print(data)
            self.write_error(errors.HTTP_BAD_REQUEST, msg='post body format error')
            return

        print(data)
        resp = json.dumps({"result": "success",})
        self.write(resp)

    def write_error(self, status_code, **kwargs):
        resp = json.dumps({
            "result": "error",
            "message": kwargs['msg']
        })
        self.write(resp)

if __name__ == '__main__':

    speaker_id = '0001'
    model_names = 'spkr0001.mdl'
    model_path = "http://huge.yiwei.callcenter.corp/models/"
    wav_path = "http://huge.yiwei.callcenter.corp/register/"
    wav_names = ["201801240004.wav", "201801240005.wav", "201801240006.wav"]

    ret = register_speaker(speaker_id, model_path, model_names, wav_path, wav_names)
