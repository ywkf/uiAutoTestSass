import hmac, base64, struct, hashlib, time
import operator
import sys
import re

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
        googleCode = hmac.new(key, msg, hashlib.sha1).digest()
        # 版本判断
        if (sys.version_info > (2, 7)):
            o = googleCode[19] & 15
        else:
            o = ord(googleCode[19]) & 15
        googleCode = str((struct.unpack(">I", googleCode[o:o + 4])[0] & 0x7fffffff) % 1000000)
        if len(googleCode) == 5:  # 如果验证码的第一位是0，则不会显示。此处判断若是5位码，则在第一位补上0
            googleCode = '0' + googleCode
        return googleCode

    # 获取 Google Code
    def get_google_code(self, text):
        secret = self.get_secret(text)
        return self.cal_google_code(secret)


if __name__ == '__main__':
    title = "otpauth://totp/HNTV%3A19977777777?secret=ne4weqjz7utzgkryur5ptgogu5oj2zig&issuer=HNTV"
    code = GetGoogleCode().get_google_code(title)
    print(code)
    secret = "zuwhrtmfuo5rrmfe6jw2yb7w3sf3jc3g"
    print(secret.upper())
