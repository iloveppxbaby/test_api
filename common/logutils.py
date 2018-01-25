#coding=utf-8
import logging
from logging.handlers import TimedRotatingFileHandler
from service.common.config import LOG_FILE


def get_logger(name=None):
    if not name:
        name = "dealer_model_service"
    logger = logging.getLogger(name)

    if not getattr(logger, 'handlers', None):
        logger.propagate = False
        pattern = '%(asctime)s %(levelname)s %(module)s.%(funcName)s Line:%(lineno)d %(message)s'
        formatter = logging.Formatter(pattern)
        handler = TimedRotatingFileHandler(filename=LOG_FILE, when='midnight', interval=1, backupCount=365)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.WARNING)

    return logger