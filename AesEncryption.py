import base64
import json
from binascii import b2a_hex, a2b_hex
from Crypto.Cipher import AES

'''
采用AES对称加密算法
'''


# # str不是32的倍数那就补足为16的倍数
# def add_to_32(value):
#     while len(value) % 32 != 0:
#         value += '\0'
#     return str.encode(value)  # 返回bytes
#
#
def add_to_16(value):
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value)  # 返回bytes





#添加补码PKCS5Padding AES加密
def AES_encrypt(secret_key,data):
    """
    :param secret_key [str] : 加密秘钥
    :param data [str] : 需要加密数据
    :return   [str] :
    """
    print(data,secret_key)
    # jsoncode = json.dumps(data).replace("(", "").replace(")", "").replace(" ", "")
    # print(jsoncode)
    BLOCK_SIZE = 16  # Bytes
    # 数据进行 PKCS5Padding 的填充
    pad = lambda s: (s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE))
    raw = pad(str(data))
    # 通过key值，使用ECB模式进行加密
    cipher = AES.new(secret_key.encode(), AES.MODE_ECB)

    # 得到加密后的字节码
    encrypted_text = cipher.encrypt(bytes(raw, encoding='utf-8'))
    # 字节码转换成base64  再转成 字符串 去掉换行符
    encrypted_text_hex = str(base64.encodebytes(encrypted_text), encoding='utf-8').replace("\n","")
    print(encrypted_text_hex)
    return encrypted_text_hex

#解码
def AES_decrypt(secret_key,encrypted_text_hex):
   """
   :param secret_key [str] : 加密秘钥
   :param encrypted_text_hex [str]: # 加密后的 data 字符串
   :return [str]:
   """
   # 去掉 PKCS5Padding 的填充
   unpad = lambda s: s[:-ord(s[len(s) - 1:])]
   # 通过 key 值进行
   cipher = AES.new(secret_key.encode(), AES.MODE_ECB)

   base64_decrypted = base64.decodebytes(encrypted_text_hex.encode(encoding='utf-8'))

   data_response = unpad(cipher.decrypt(base64_decrypted).decode('utf-8')).rstrip("\0")
   #print(data_response)
   return data_response








if __name__ == '__main__':

    key = "ehJzGST0D8Ne6adg"



    jsonText = {"apiKey":"93960537348","apiSecret":"ehJzGST0D8Ne6adg"}


    #jsoncode  = json.dumps(jsonText).replace("(","").replace(")","").replace(" ","")
    #print(jsoncode)

    encrytext = AES_encrypt(key,jsonText)

    AES_decrypt(key,encrytext)
