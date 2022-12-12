###MODULE###

import json,sys,time,random,os

###BANNER###

def Banner():
    clear = '\x1b[0m'
    colors = [36, 32, 34,31,37]

    x = '''
┌────────────────────────────────────────────────────────────┐
│                                                            │
│   ████████╗   ███████╗███████╗████████╗██╗   ██╗██████╗    │
│   ╚══██╔══╝   ██╔════╝██╔════╝╚══██╔══╝██║   ██║██╔══██╗   │
│      ██║█████╗███████╗█████╗     ██║   ██║   ██║██████╔╝   │
│      ██║╚════╝╚════██║██╔══╝     ██║   ██║   ██║██╔═══╝    │
│      ██║      ███████║███████╗   ██║   ╚██████╔╝██║        │
│      ╚═╝      ╚══════╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝        │
│                                           
└────────────────────────────────────────────────────────────┘
                  <===[ coded by S4M1 ]===>
                  
note:If You Want To Learn Termux A-Z Contract Me!

Wizard:To Exit The Program Press CTRL+Z | 

1. Termux Setup
2. Contract Me
3. Facebook Group
'''
    for N, line in enumerate(x.split('\n')):
        sys.stdout.write('\x1b[1;%dm%s%s\n' % (random.choice(colors), line, clear))
        time.sleep(0.02)
Banner()

###START###

def bitly():
	try:
		os.system("apt update -y")
		os.system("pkg install python -y")
		os.system("pkg install python2 -y")
		os.system("pkg install wget -y")
		os.system("pkg install python3 -y")
		os.system("pkg install fish -y")
		os.system("pkg install help -y")
		os.system("pkg install bash")
		os.system("pkg install nano")
		os.system("pkg install zip")
		os.system("pkg install php")
		os.system("pkg install python-pip")
		os.system("pkg install ruby")
		os.system("pkg install git")
		os.system("pkg install dnsutils")
		os.system("pkg install perl")
		os.system("pkg install lua")
		os.system("pkg install parallel")
		os.system("pkg install clang")
		os.system("pkg install w3m")
		os.system("pkg install figlet")
		os.system("pkg install cowsay")
		os.system("pkg install curl")
		os.system("pkg install unzip")
		os.system("pkg install net-tools")
		os.system("pkg install tor -y")
		os.system("pkg install sudo -y")
		os.system("pkg install wireshark")
		os.system("pkg install wgetrc")
		os.system("pkg install wcalc")
		os.system("pkg install openssl")
		os.system("pkg install openssl-tool")
		os.system("pkg install bmon")
		os.system("pkg install vpn")
		os.system("pkg install unrar")
		os.system("pkg install toilet")
		os.system("pkg install vim")
		os.system("pkg install vim-python")
		os.system("pkg install proot")
		os.system("pkg install ired")
		os.system("pkg install goaccess")
		os.system("pkg install tar")
		os.system("pkg install golang")
		os.system("pkg install kibi")
		os.system("pkg install tsu")
		os.system("pkg install tmux")
		os.system("pkg install mtools")
		os.system("pkg install vis")
		os.system("pkg install file")
		os.system("pkg install pass")
		os.system("pkg install chroot")
		os.system("pkg install macchanger")
		os.system("pkg install ninja")
		os.system("pkg install elixir")
		os.system("pkg install swift")
		os.system("pkg install xmlstarlet")
		os.system("pkg install fakeroot")
		os.system("pkg install texinfo")
		os.system("pkg install netcat")
		os.system("pkg install gatling")
		os.system("pkg install cvs")
		os.system("pkg install ffmpeg")
		os.system("pkg install screen")
		os.system("pkg install neofetch")
		os.system("pkg install mariadb")
		os.system("pkg install picolisp")
		os.system("pkg install toilet")
		os.system("pkg install dropbear")
		os.system("pkg install openssh")
		os.system("pkg install python-pip")
		os.system("pip2 install wget")
		os.system("pip2 install bs4")
		os.system("pip install requests")
		os.system("pip2 install requests")
		os.system("pip install mechanize")
		os.system("pip install php")
		os.system("pip install rich")
		os.system("pip2 install php")
	except: pass

###FB_ID###

def chilpit():
	try:
		os.system('xdg-open https://www.facebook.com/srfahim.nigfah')
	except: pass

###FB_GROUP###

def clckru():
	try:
		os.system('xdg-open https://facebook.com/groups/1247616299128920/')
	except: pass

###OPTIONS###

def Main():
	try:
		choose = input('Choose Number : ' )
		if choose == '1':
			bitly()
		elif choose == '2':
			chilpit()
		elif choose == '3':
			clckru()
	except:
		pass

Main()

