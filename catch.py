import re
from Cryptodome.Cipher import AES
from base64 import b64encode
import requests
import json

song = []
song1 = []
def catch_songlist(uid):
    song2 = []
    song2.clear()
    url = "https://music.163.com/weapi/v1/play/record?csrf_token="
    uid = uid

    data = {
        "csrf_token": "",
        "limit": "1000",
        "offset": "0",
        "total": "true",
        "type": "-1",
        # "uid": "409649088"
        "uid": uid
    }

    e = '010001'
    f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
    g = '0CoJUm6Qyw8W8jud'
    i = "IiBm4sfw4wIlo7uu"

    def get_encSecKey():
        return "cd7befb975a455de0176d60d1f5ae94df5fa50c2dc93be275894dc76ee89ec3bfd134920baa6c2213be5fc00cf87047cfaaa0aa946b09bf3145cf2abb9186e075e836663b45449e5510c546e28ba3307ca5ebeb6d15d9987ddbf4863176216968603d7a99f75ce355b120ca1dcdd398ace03b75fbd0c0da2a384de2cdc101894"

    def get_params(data):
        first = enc_params(data, g)
        second = enc_params(first, i)
        return second

    def to_16(data):
        pad = 16 - len(data) % 16
        data += chr(pad) * pad
        return data

    def enc_params(data, key):
        iv = "0102030405060708"
        data = to_16(data)
        aes = AES.new(key=key.encode("utf-8"), IV=iv.encode('utf-8'), mode=AES.MODE_CBC)
        bs = aes.encrypt(data.encode("utf-8"))
        return str(b64encode(bs), "utf-8")

    resp = requests.post(url, data={
        "params": get_params(json.dumps(data)),
        "encSecKey": get_encSecKey()
    })
    obj = re.compile(r'"song".*?"name":"(?P<name>.*?)","id".*?"ar":.*?"name":"(?P<artist>.*?)","tns"', re.S)
    res = obj.finditer(resp.text)
    res1 = obj.finditer(resp.text)
    for i in res:
        song1.append(i.group("name") + '------' + i.group("artist"))
    for i in res1:
        # song2.append(i.group("name"))
        song2.append(i.group("name") + '------' + i.group("artist"))
    return song2




