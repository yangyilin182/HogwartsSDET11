import json

import requests

from homework20200412.api.base_api import BaseApi


class WeWork(BaseApi):
    token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    corpid = 'wwf5d5f507b6393282'
    token = dict()
    token_time = dict
    # 客户联系secret
    secret = 'l5Chq52ozBKSXd5QgrvdrVBUjZzeY3yWUOfSfCE5bXo'

    @classmethod
    def get_token(cls, secret=secret):
        # todo:
        if secret is None:
            # todo: token制度发生变化，在这个地方决定是否重新获取
            return cls.token[secret]
        # 避免重复请求，提高速度
        if secret not in cls.token.keys():
            r = cls.get_access_token(secret)
            cls.token[secret] = r["access_token"]

        return cls.token[secret]

    @classmethod
    def get_access_token(cls, secret):
        r = requests.get(
            cls.token_url,
            params={"corpid": cls.corpid, "corpsecret": secret}
        )
        cls.format(r)
        return r.json()
