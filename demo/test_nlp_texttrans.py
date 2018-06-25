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
    str_text = '一个演员的演技能烂到什么程度？'
    type = 0
    ai_obj = apiutil.AiPlat(app_id, app_key)

    print('----------------------SEND REQ----------------------')
    rsp = ai_obj.getNlpTextTrans(str_text, type)
    if rsp['ret'] == 0:
        print(json.dumps(rsp, ensure_ascii=False, sort_keys=False, indent=4))
        print('----------------------API SUCC----------------------')
    else:
        print(json.dumps(rsp,  ensure_ascii=False, sort_keys=False, indent=4))
        # print rsp
        print('----------------------API FAIL----------------------')

