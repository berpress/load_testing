import random
import string
from datetime import datetime


class UtilHelper:

    @staticmethod
    def get_random_string(length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    @staticmethod
    def get_current_time_stamp():
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        return timestamp

    @staticmethod
    def get_base_header():
        base_header = {
            'Content-type': 'application/x-www-form-urlencoded',
            'Connection': 'keep-alive'
        }
        return base_header

    @staticmethod
    def get_base_header_with_cookie(cookie):
        cookie_header = UtilHelper.get_base_header()
        cookie_str = ""
        for item in cookie.iteritems():
            cookie_str += item[0] + "=" + item[1]
        cookie_header['Cookie'] = cookie_str
        return cookie_header
