import os
import sys
import argparse
import traceback
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

sys.path.append(os.path.join(os.path.split(os.path.abspath(__file__))[0], '..'))

import service.common.errors as errors
import service.engine.engine_store as engine_store

from service.handler.dealer_handler import DealerModelHandler
from service.handler.health_handler import HealthHandler

# g3 example
# curl --request POST --url http://localhost:8000/check --header 'content-type: application/json' --data '{"type":"phone", "identities":["053683420000000000"]}'
# response {"result": "success", "data": [{"phone": ["053683420000000000"], "isAucxtion": false}]}

def create_application():
    try:
        # load global singleton model
        _ = engine_store.EngineStore.get_inited_store()
    except errors.CLFModelInitializedError as e:
        print(str(e), traceback.format_exc(), file=sys.stderr)
    except errors.FeaExtractorInitializedError as e:
        print(str(e), traceback.format_exc(), file=sys.stderr)

    application = tornado.web.Application(
        [
            (r"/", HealthHandler),
            (r"/check", DealerModelHandler)
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

