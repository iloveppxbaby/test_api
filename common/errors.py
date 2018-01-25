HTTP_SUCCESS = 200
HTTP_BAD_REQUEST = 400
HTTP_INTERNAL_ERROR = 500


class LambdaInitializedError(Exception):
    def __init__(self, msg):
        self.msg = msg
        self.error_code = HTTP_INTERNAL_ERROR

    def __str__(self):
        return "%s: %s" % (str(self.__class__.__name__), self.msg)


class FeatureExtractionError(Exception):
    def __init__(self, msg):
        self.msg = msg
        self.error_code = HTTP_INTERNAL_ERROR

    def __str__(self):
        return "%s: %s" % (str(self.__class__.__name__), self.msg)
