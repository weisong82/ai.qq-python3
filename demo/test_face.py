# -*- coding: UTF-8 -*-
import json
from configparser import ConfigParser

import apiutil

cf = ConfigParser()
cf.read("../SDK/key.conf")

app_key = cf.get("default","app_key")
app_id = cf.get("default","app_id")


# https://ai.qq.com/doc/detectface.shtml
if __name__ == '__main__':
    with open('../data/fbb.jpeg', 'rb') as bin_data:
        image_data = bin_data.read()

    ai_obj = apiutil.AiPlat(app_id, app_key)
    rsp = ai_obj.face_detectface(image_data, 0)

    if rsp['ret'] == 0:
        print(json.dumps(rsp, ensure_ascii=False, sort_keys=False, indent=4))
        print('----------------------API SUCC----------------------')
    else:
        print(json.dumps(rsp,  ensure_ascii=False, sort_keys=False, indent=4))
        # print rsp
        print('----------------------API FAIL----------------------')
