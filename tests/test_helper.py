import os
import random

import re
from datetime import timedelta, tzinfo

SUFFIX = os.environ.get('TRAVIS_JOB_ID') or random.randint(10000, 99999)
REMOTE_TEST_IMAGE = "http://cloudinary.com/images/old_logo.png"
REMOTE_TEST_IMAGE_UNICODE = u"http://cloudinary.com/images/old_logo.png"
RESOURCE_UPLOAD_TYPES = ['facebook', 'fetch', 'multi', 'sprite', 'text', 'twitter_name', 'upload']
TEST_IMAGE = "tests/logo.png"
TEST_TAG = "pycloudinary_test"
UNIQUE_TAG = "{0}_{1}".format(TEST_TAG, SUFFIX)

ZERO = timedelta(0)

# A UTC class.

class UTC(tzinfo):
    """UTC"""

    def utcoffset(self, dt):
        return ZERO

    def tzname(self, dt):
        return "UTC"

    def dst(self, dt):
        return ZERO


def get_method(mocker):
    return mocker.call_args[0][0]


def get_uri(args):
    return args[1]


def get_params(args):
    return args[2] or {}


def get_param(mocker, name):
    """
    Return the value of the parameter
    :param mocker: the mocked object
    :param name: the name of the paramer
    :return: the value of the parameter if present or None
    """
    args, kargs = mocker.call_args
    params = get_params(args)
    return params.get(name)


def get_list_param(mocker, name):
    """
    Return a list of values for the given param name
    :param mocker: the mocked object
    :param name: the name of the parameter
    :return: a list of values
    """
    args, kargs = mocker.call_args
    params = get_params(args)
    reg = re.compile(r'{}\[\d*\]'.format(name))
    return [params[key] for key in params.keys() if reg.match(key)]


def get_unique_public_id(res_upload_type='upload', suffix=''):
    if not res_upload_type in RESOURCE_UPLOAD_TYPES:
        res_upload_type = 'upload'
    return '{0}_{1}_{2}'.format(TEST_TAG, res_upload_type, suffix)
