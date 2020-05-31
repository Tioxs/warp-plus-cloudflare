import urllib.request
import json
import datetime
import random
import string
import time
import os
import sys
os.system("title WARP-PLUS-CLOUDFLARE - XORCAN v3")
os.system('cls' if os.name == 'nt' else 'clear')
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
	try:
		letters = string.ascii_letters + string.digits
		return ''.join(random.choice(letters) for i in range(stringLength))
	except Exception as error:
		print(error)		    
def digitString(stringLength):
	try:
		digit = string.digits
		return ''.join((random.choice(digit) for i in range(stringLength)))    
	except Exception as error:
		print(error)	
url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'
def run():
	try:
		install_id = genString(11)
		body = {"key": "{}=".format(genString(42)),
				"install_id": install_id,
				"fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
				"referrer": referrer,
				"warp_enabled": False,
				"tos": datetime.datetime.now().isoformat()[:-3] + "+07:00",
				"type": "Android",
				"locale": "zh-CN"}
		data = json.dumps(body).encode('utf8')
		headers = {'Content-Type': 'application/json; charset=UTF-8',
					'Host': 'api.cloudflareclient.com',
					'Connection': 'Keep-Alive',
					'Accept-Encoding': 'gzip',
					'User-Agent': 'okhttp/3.12.1'
					}
		req         = urllib.request.Request(url, data, headers)
		response    = urllib.request.urlopen(req)
		status_code = response.getcode()	
		return status_code
	except Exception as error:
		print(error)	

g = 0
b = 0
while True:
	result = run()
	if result == 200:
		g = g + 1
		os.system('cls' if os.name == 'nt' else 'clear')
		print("")
		print("WARP-PLUS-CLOUDFLARE (script)" + " By ALIILAPRO / xorcan v3")
		print("")
		animation = ["[■□□□□□□□□□] 10%","[■■□□□□□□□□] 20%", "[■■■□□□□□□□] 30%", "[■■■■□□□□□□] 40%", "[■■■■■□□□□□] 50%", "[■■■■■■□□□□] 60%", "[■■■■■■■□□□] 70%", "[■■■■■■■■□□] 80%", "[■■■■■■■■■□] 90%", "[■■■■■■■■■■] 100%"] 
		for i in range(len(animation)):
			time.sleep(0.5)
			sys.stdout.write("\r[+] Hazırlanıyor... " + animation[i % len(animation)])
			sys.stdout.flush()
		print(f"\n[-] Şu kimlik üzerinde çalışılıyor: {referrer}")    
		print(f"[:)] {g} GB kullanım hakkı hesabınıza eklendi")
		print(f"[#] Toplam: {g} Başarılı {b} Başarısız")
		print("[*] 18 saniye sonra yeni istek gönderilecek.")
		time.sleep(18)
	else:
		os.system('cls' if os.name == 'nt' else 'clear')
		print("")
		print("WARP-PLUS-CLOUDFLARE (script)" + " By ALIILAPRO / xorcan v3")
		print("")
		print("[:(] Sunucuya bağlanırken hata oluştu")
		print(f"[#] Toplam: {g} Başarılı {b} Başarısız")
		b = b + 1	
