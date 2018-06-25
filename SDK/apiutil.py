# -*- coding: UTF-8 -*-
import hashlib
import urllib
from urllib import parse
import urllib.request
import base64
import json
import time

url_preffix='https://api.ai.qq.com/fcgi-bin/'


def setParams(array, key, value):
    array[key] = value


def genSignString(parser):
    uri_str = ''
    for key in sorted(parser.keys()):
        if key == 'app_key':
            continue
        uri_str += "%s=%s&" % (key, parse.quote(str(parser[key]), safe=''))
    sign_str = uri_str + 'app_key=' + parser['app_key']

    hash_md5 = hashlib.md5(sign_str.encode('utf-8'))
    return hash_md5.hexdigest().upper()


class AiPlat(object):
    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key
        self.data = {}
        self.url_data = ''

    def invoke(self, params):
        self.url_data = urllib.parse.urlencode(params).encode("utf-8")
        req = urllib.request.Request(self.url, self.url_data)
        try:
            rsp = urllib.request.urlopen(req)
            str_rsp = rsp.read().decode('utf-8')
            dict_rsp = json.loads(str_rsp)
            return dict_rsp
        except Exception as e:
            print(e)
            return {'ret': -1}


    def face_detectface(self, image, mode):
        self.url = url_preffix + 'face/face_detectface'
        setParams(self.data, 'app_id', self.app_id)
        setParams(self.data, 'app_key', self.app_key)
        setParams(self.data, 'mode', mode)
        setParams(self.data, 'time_stamp', int(time.time()))
        setParams(self.data, 'nonce_str', int(time.time()))
        image_data = base64.b64encode(image)
        setParams(self.data, 'image', image_data.decode("utf-8"))
        sign_str = genSignString(self.data)
        setParams(self.data, 'sign', sign_str)
        return self.invoke(self.data)

    def getOcrGeneralocr(self, image):
        self.url = url_preffix + 'ocr/ocr_generalocr'
        setParams(self.data, 'app_id', self.app_id)
        setParams(self.data, 'app_key', self.app_key)
        setParams(self.data, 'time_stamp', int(time.time()))
        setParams(self.data, 'nonce_str', int(time.time()))
        image_data = base64.b64encode(image)
        setParams(self.data, 'image',  image_data.decode("utf-8"))
        sign_str = genSignString(self.data)
        setParams(self.data, 'sign', sign_str)
        return self.invoke(self.data)

    def getNlpTextTrans(self, text, type):
        self.url = url_preffix + 'nlp/nlp_texttrans'
        setParams(self.data, 'app_id', self.app_id)
        setParams(self.data, 'app_key', self.app_key)
        setParams(self.data, 'time_stamp', int(time.time()))
        setParams(self.data, 'nonce_str', int(time.time()))
        setParams(self.data, 'text', text)
        setParams(self.data, 'type', type)
        sign_str = genSignString(self.data)
        setParams(self.data, 'sign', sign_str)
        return self.invoke(self.data)

    def getAaiWxAsrs(self, chunk, speech_id, end_flag, format_id, rate, bits, seq, chunk_len, cont_res):
        self.url = url_preffix + 'aai/aai_wxasrs'
        setParams(self.data, 'app_id', self.app_id)
        setParams(self.data, 'app_key', self.app_key)
        setParams(self.data, 'time_stamp', int(time.time()))
        setParams(self.data, 'nonce_str', int(time.time()))
        speech_chunk = base64.b64encode(chunk)
        setParams(self.data, 'speech_chunk', speech_chunk.decode("utf-8"))
        setParams(self.data, 'speech_id', speech_id)
        setParams(self.data, 'end', end_flag)
        setParams(self.data, 'format', format_id)
        setParams(self.data, 'rate', rate)
        setParams(self.data, 'bits', bits)
        setParams(self.data, 'seq', seq)
        setParams(self.data, 'len', chunk_len)
        setParams(self.data, 'cont_res', cont_res)
        sign_str = genSignString(self.data)
        setParams(self.data, 'sign', sign_str)
        return self.invoke(self.data)
