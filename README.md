# sınırsız warp+ verisi alma yöntemi
![Code Size](https://img.shields.io/github/languages/code-size/xorcan/warp-plus-cloudflare) ![Top Language](https://img.shields.io/github/languages/top/xorcan/warp-plus-cloudflare) ![GitHub stars](https://img.shields.io/github/stars/xorcan/warp-plus-cloudflare)

![](https://github.com/xorcan/warp-plus-cloudflare/raw/master/pic.png)

**not: bu betik benim tarafımdan yazılmamıştır. sadece tamamlanmış, türkçeleştirilmiş ve "tek başına çalıştırılabilirlik" eklenmiştir.** 😉

### bu komut dosyasıyla 1.1.1.1 warp+ hesabınızı süresiz olarak reşarj edebilirsiniz. 📱

### [?] warp+ nedir?
warp+, daha yüksek hızlar elde etmek ve bağlantınızın internet'in uzun vadede şifrelenmesini sağlamak için cloudflare’nin argo olarak bilinen sanal özel omurgasını kullanır. [daha fazla bilgi (ingilizce)](https://blog.cloudflare.com/announcing-warp-plus/)

### [?] betik nasıl kullanılır? *( windows, mac, linux )*
- öncelikle python'u sisteminize kurun. [python 3.8+](https://www.python.org/downloads/)
- - windows 10 kullanıyorsanız: 
- - herhangi bir klasörde shift tuşuyla birlite sağ tıklayıp powershell'i açın
- - `python` yazın ve enterlayın, sizi mağazaya yönlendirecek.
- - yönlendirse de yönlendirmese de mağazadan python'u ayrıca indirip kurun.
- modül isteklerini yükleyelim:
- aynı yöntemlerle cmd / terminale kopyalayın ve enterlayın: `pip install requests`
- [buradan](https://github.com/xorcan/warp-plus-cloudflare/archive/master.zip) projeyi indirin ve çıkartın (unzip)
- ayıklanan dizinde bir cmd / terminal / kabuk açın
- şu satırı girin: `python warp1.py`
- komut dosyasını çalıştırın ve kullanın

### [?] tek başına çalışabilir betik (v2)
- normal bir kullanıcı için yukarıdaki gayet iyidir. bu sürümü yalnızca ne yaptığınızı biliyorsanız kullanın.
- teknik olarak hiçbir fark yok. ancak bu sürümdeki dosya tek komutta işinizi halleder.
- ayrıca size kimlik sormaz, rahatsız etmez.
- `warp2.py` dosyasını bir düzenleyici ile açın ve `xorcan` değeri yerine warp+ kimliğinizi yazıp kaydedin.
- çalıştırmak için: `python warp2.py`

![](https://github.com/xorcan/warp-plus-cloudflare/blob/master/win.jpg)

### [?] androidde çalıştırmak

- [termux](https://play.google.com/store/apps/details?id=com.termux&hl=tr) uygulamasını yükleyin, açın ve şu komutları sıra sıra girin (kopyalayıp yapıştırabilirsiniz):
- `pkg install git`
- `pkg install python`
- `pip install requests`
- ardından şu komutla giti kendi cihazınıza klonlayın (indirin): 
- `git clone https://github.com/xorcan/warp-plus-cloudflare.git`
- betiğin dizinini açın:
- `cd warp-plus-cloudflare`
- betiği çalıştını:
- `python warp{sürüm numarası}.py`

### [?] warp+ kimliğini (id) nasıl alırım?

1. 1.1.1.1 uygulamasını açın.
2. menü (üç nokta) işaretine tıklayın ☰
3. gelişmiş (advanced) > tanılamalar (diagonistics)
4. i̇stemci yapılandırması (client configuration)'nın altındaki kimlik (id) > basılı tutun ve kopyalayın.

![](https://github.com/xorcan/warp-plus-cloudflare/blob/master/id.jpg)
