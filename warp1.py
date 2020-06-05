import urllib.request
import json
import datetime
import random
import string
import time
import os
import sys
import pathlib
script_version = '3.0.0'
window_title   = f"WARP-PLUS-CLOUDFLARE by ALIILAPRO / XORCAN (v {script_version})"
os.system('title ' + window_title if os.name == 'nt' else 'PS1="\[\e]0;' + window_title + '\a\]"; echo $PS1')
os.system('cls' if os.name == 'nt' else 'clear')
print ("---------------------------------------------------------------------------")
print ("[1] 1.1.1.1 için sınırsız WARP+ verisi alma - normal sürüm")
print ("---------------------------------------------------------------------------")
print ("[?] S; WARP+ kimliği (id) nasıl alınır?")
print ("[-] C; 1.1.1.1 uygulamasından: [ Ayarlar/Gelişmiş/Tanılamalar/Kimlik ]")
print ("[-] C; Bu yolu izleyip Kimlik kısmındaki koda basılı tutarak kopyalayın")
print ("---------------------------------------------------------------------------")
print ("[?] S; Daha açıklayıcı birşey yok mu?")
print ("[-] C; Birisi güzelce anlatmış: [ is.gd/birbir ]")
print ("---------------------------------------------------------------------------")
print ("[i] bu sürüm, kimlik girmenizi isteyerek çalışır.")
print ("[i] soru sormadan çalışan sürüm de mevcut: [warp2.py]")
print ("---------------------------------------------------------------------------")
print ("[i] aliilapro tarafından yazıldı [ aliilapro.github.io ]")
print ("[i] xorcan tarafından türkçeleştirildi [ github.com/xorcan ]")
print ("[i] anlatımı hazırlayan kişiye teşekkürler: anonim")
print ("---------------------------------------------------------------------------")

def newID():
	while True:
		referrer  = input("[#] WARP+ Kimliğinizi girin:")
		user_input = input(f"[?] Kimliğiniz: {referrer} doğru mu? (e/h):")
		if user_input == "e":
			save_id = input("[?] Kimliğinizi kaydetmek ister misiniz? (e/h):")
			if save_id == "e":
			    with open("referrer.txt","w") as file:
				    file.write(referrer)
			    return referrer
			elif save_id == "h":
				return referrer
			else:
			    print(f"\"{save_id}\" geçerli bir parametre değil.")
		elif user_input == "h":
			user_input = None
		else:
			print(f"\"{user_input}\" geçerli bir parametre değil.")

def progressBar():
	animation     = ["[□□□□□□□□□□]","[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]"]
	progress_anim = 0
	save_anim     = animation[progress_anim % len(animation)]
	percent       = 0
	while True:
		for i in range(10):
			percent += 1
			sys.stdout.write(f"\r[+] Yanıt bekleniyor... " + save_anim + f" {percent}%")
			sys.stdout.flush()
			time.sleep(0.075)
		progress_anim += 1
		save_anim = animation[progress_anim % len(animation)]
		if percent == 100:
			sys.stdout.write("\r[+] İstek tamamlandı... [■■■■■■■■■■] %100")
			break

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
		install_id = genString(22)
		body = {"key": "{}=".format(genString(43)),
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
		print("")
		print(error)	

if pathlib.Path("referrer.txt").exists():
	while True:
		user_input = input("[?] Kaydedilmiş warp+ kimliğini kullanmak ister misiniz? (e/h):")
		if user_input == "e":
			with open("referrer.txt","r") as file:
				referrer = file.read().strip()
			break
		elif user_input == "h":
			referrer = newID()
			break
		else:
			print(f"\"{user_input}\" geçerli bir parametre değil.")
else:
	referrer = newID()

g = 0
b = 0
while True:
	os.system('cls' if os.name == 'nt' else 'clear')
	print("")
	print("WARP-PLUS-CLOUDFLARE (betik)" + " by ALIILAPRO / XORCAN v3")
	print("")
	sys.stdout.write("\r[+] İstek gönderiliyor... [□□□□□□□□□□] %0")
	sys.stdout.flush()
	result = run()
	if result == 200:
		g += 1
		progressBar()
		print(f"\n[-] Şu kimlik üzerinde çalışılıyor: {referrer}")    
		print(f"[:)] {g} GB kullanım hakkı hesabınıza eklendi")
		print(f"[#] Toplam: {g} Başarılı {b} Başarısız")
		for i in range(18,0,-1):
			sys.stdout.write(f"\r[*] {i} saniye sonra yeni bir istek gönderilecek")
			sys.stdout.flush()
			time.sleep(1)
	else:
		b += 1
		print("[:(] Sunucuya bağlanırken hata oluştu")
		print(f"[#] Toplam: {g} Başarılı {b} Başarısız")
		for i in range(10,0,-1):
			sys.stdout.write(f"\r[*] {i} saniye içinde tekrar deneniyor...")
			sys.stdout.flush()
			time.sleep(1)
