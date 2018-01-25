# coding=utf8

import os

ROOT_DIR = os.path.join(os.path.split(os.path.abspath(__file__))[0], '..')
LAMBDA_DIR = os.path.join(ROOT_DIR, 'lambda')
LOG_FILE = os.path.join(ROOT_DIR, 'service.log')

CODE_SUCCESS = "success"
CODE_ERROR = "error"

