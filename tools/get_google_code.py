import datetime
import hmac, base64, struct, hashlib, time
import operator
import sys
import re

import pyperclip

import page


class GetGoogleCode:

    # 截取 secret
    def get_secret(self, text):
        pattern = r"\?secret=(.+?)\&issuer="
        secret = re.findall(pattern, text)
        return secret[0]

    # 计算 Google Code
    def cal_google_code(self, secret):
        secret = secret.upper()
        input = int(time.time()) // 30
        key = base64.b32decode(secret)
        msg = struct.pack(">Q", input)
        google_code = hmac.new(key, msg, hashlib.sha1).digest()
        # 版本判断
        if (sys.version_info > (2, 7)):
            o = google_code[19] & 15
        else:
            o = ord(google_code[19]) & 15
        google_code = str((struct.unpack(">I", google_code[o:o + 4])[0] & 0x7fffffff) % 1000000)

        # if len(google_code) == 5:  # 如果验证码的第一位是0，则不会显示。此处判断若是5位码，则在第一位补上0
        #     google_code = '0' + google_code

        google_code = google_code.zfill(6)

        return google_code

    # 获取 Google Code
    def get_google_code(self, text):
        secret = self.get_secret(text)
        return self.cal_google_code(secret)


if __name__ == '__main__':
    title = "otpauth://totp/HNTV%3A19977777777?secret=ne4weqjz7utzgkryur5ptgogu5oj2zig&issuer=HNTV"
    code = GetGoogleCode().get_google_code(title)
    print(code)
    secret = "6co73ayr4rnquvaxca427rgp24av3ssc"
    print(secret.upper())




    









