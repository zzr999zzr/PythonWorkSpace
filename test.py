#!-*- /usr/bin/python -*-
#!-*- coding = utf-8 -*-
#@Athor : Alfa
#@TIME : 2020/4/9 0009 11:02
#@FILE : test.PY
import json

jsonText = {
    "apikey": "8178407429186237",
    "apiSecret": "8beb33c01d2d43f4bd3895389222362c"
}
jsoncode = json.dumps(jsonText)
print(jsoncode)