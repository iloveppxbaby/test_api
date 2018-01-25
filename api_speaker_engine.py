import os
import sys
import argparse
import traceback
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import common.errors as errors
import engine.engine_store as engine_store

from handler.register_handler import RegisterHandler
from handler.test_handler import TestHandler

# api example
# curl --request POST --url http://localhost:8030/register --header 'content-type: application/json'
# --data '{"speaker_id": 0001,
#          "wav_path": "http://huge.yiwei.callcenter.corp/register/"
#          "wav_names": ["201801240001.wav", "201801240002.wav", "201801240003.wav"],
#          "model_path": "http://huge.yiwei.callcenter.corp/models/",
#          "model_name": "spkr0001.mdl"}'
# response: {"result": "success"}
#        or {'result': "error", 'data': 'error_msg'}
#
#
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


def create_application():
    # try:
    #     _ = engine_store.EngineStore.get_inited_store()
    # except errors.LambdaInitializedError as e:
    #     print(str(e), traceback.format_exc(), file=sys.stderr)
    #     raise e

    application = tornado.web.Application(
        [
            (r"/register", RegisterHandler),
            (r"/test", TestHandler)
        ],
    )
    return application

app = create_application()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default="8030")
    args = parser.parse_args()

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(args.port)
    tornado.ioloop.IOLoop.instance().start()

