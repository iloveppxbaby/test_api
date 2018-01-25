import os
from sklearn.externals import joblib
from common import errors
from common import config


class _EngineStore(object):

    def __init__(self):
        self._initialized = False
        self.ubm = None

    def _initialize_lambda(self, lambda_path):
        fn = os.path.join(lambda_path, 'ubm_file')
        try:
            self.ubm = joblib.load(fn)
        except:
            raise errors.LambdaInitializedError('ubm_file:{0} load failed'.format(fn))

    def ensure_initialized(self):
        if not self._initialized:
            self._initialize_lambda(config.LAMBDA_DIR)
            self._initialized = True

    def get_ubm(self):
        return self.ubm


class EngineStore(object):
    store = _EngineStore()

    @staticmethod
    def get_inited_store():
        EngineStore.store.ensure_initialized()
        return EngineStore.store

