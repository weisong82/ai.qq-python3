#-*- coding: UTF-8 -*-
import sys
from configparser import ConfigParser

sys.path.append('../SDK')
import apiutil
import json

cf = ConfigParser()
cf.read("../SDK/key.conf")

app_key = cf.get("default","app_key")
app_id = cf.get("default","app_id")


if __name__ == '__main__':
    with open('../data/generalocr.jpg', 'rb') as bin_data:
        image_data = bin_data.read()

    ai_obj = apiutil.AiPlat(app_id, app_key)

    print('----------------------SEND REQ----------------------')
    rsp = ai_obj.getOcrGeneralocr(image_data)

    if rsp['ret'] == 0:
        for i in rsp['data']['item_list']:
            print(i['itemstring'])
        print('----------------------API SUCC----------------------')
    else:
        print(json.dumps(rsp, ensure_ascii=False, sort_keys=False, indent=4))
        print('----------------------API FAIL----------------------')
