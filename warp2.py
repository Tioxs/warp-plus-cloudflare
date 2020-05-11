import requests
import json
import datetime
import random
import string
import time
print ("---------------------------------------------------------------------------")
print ("[2] 1.1.1.1 için sınırsız WARP+ verisi metodu - sorusuz sürüm")
print ("---------------------------------------------------------------------------")
print ("[?] S; WARP+ kimliği (id) nasıl alınır?")
print ("[-] C; 1.1.1.1 uygulamasından: [ Ayarlar/Gelişmiş/Tanılamalar/Kimlik ]")
print ("[-] C; Bu yolu izleyip Kimlik kısmındaki koda basılı tutarak kopyalayın")
print ("---------------------------------------------------------------------------")
print ("[?] S; Daha açıklayıcı birşey yok mu?")
print ("[-] C; Birisi güzelce anlatmış: [ is.gd/birbir ]")
print ("---------------------------------------------------------------------------")
print ("[i] bu sürüm, tek başına (sorusuz) çalıştırılabilir.")
print ("[i] 25. satırdaki xorcan yerine warp+ kimliğinizi yazın ve çalıştırın")
print ("[i] ne yaptığınızı bilmiyorsanız normal sürümü kullanın [warp1.py]")
print ("---------------------------------------------------------------------------")
print ("[i] aliilapro tarafından yazıldı [ aliilapro.github.io ]")
print ("[i] xorcan tarafından türkçeleştirildi [ github.com/xorcan ]")
print ("[i] anlatımı hazırlayan kişiye teşekkürler: anonim")
print ("---------------------------------------------------------------------------")
referrer = "xorcan"
def genString(stringLength):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))
def digitString(stringLength):
    digit = string.digits
    return ''.join((random.choice(digit) for i in range(stringLength)))    
url = f'http://api.cloudflareclient.com/v0a{digitString(3)}/reg'
def run():
    install_id = genString(11)
    body = {"key": "{}=".format(genString(42)),
            "install_id": install_id,
            "fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
            "referrer": referrer,
            "warp_enabled": False,
            "tos": datetime.datetime.now().isoformat()[:-3] + "+07:00",
            "type": "Android",
            "locale": "zh-CN"}
    bodyString = json.dumps(body)
    headers = {'Content-Type': 'application/json; charset=UTF-8',
               'Host': 'api.cloudflareclient.com',
               'Connection': 'Keep-Alive',
               'Accept-Encoding': 'gzip',
               'User-Agent': 'okhttp/3.12.1'
               }
    r = requests.post(url, data=bodyString, headers=headers)
    return r
c = 1
while True:
    result = run()
    if result.status_code == 200:
        print(f"\n{c} GB kullanım hakkı hesabınıza eklendi")
        c = c + 1
        time.sleep(20)
    else:
        print("Sunucuya bağlanırken hata oluştu")

