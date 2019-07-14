import json , sys , hashlib , os , time , marshal
###################################################################
###################################################################
#                             COLOR

if sys.platform in ["linux","linux2"]:
	W = "\033[0m"
        G = '\033[32;1m'
        R = '\033[31;1m'
else:
	W = ''
	G = ''
	R = ''
###################################################################
#                      Exception
try:
	import requests
except ImportError:
	print
	print
	print "Can't import module 'requests'"
	print
	os.system ("sh install.sh")
####################################################################
#                    Set Default encoding
reload (sys)
sys . setdefaultencoding ( 'utf8' )
####################################################################
#       	        I don't know
jml = []
jmlgetdata = []
n = []
####################################################################
#                        BANNER
def baliho():
	try:
		token = open('.cookie/token.log','r').read()
		r = requests.get('https://graph.facebook.com/me?access_token=' + token)
		a  = json.loads(r.text)
		hname = a['name']
		n.append(a['name'])

		print ' '
		print ('[!] ' + name +' [!]').center(44)
		print ' '

	except (KeyError,IOError):
		print ' '
		print (G+ '    Get Your Token')
		print ' '

def get(data):
	print '[*] Generate access token '

	try:
		os.mkdir('.cookie')
	except OSError:
		pass

	b = open('.cookie/token.log','w')
	try:
		r = requests.get('https://api.facebook.com/restserver.php',params=data)
		a = json.loads(r.text)

		b.write(a['access_token'])
		b.close()
		print '[*] successfully generate access token'
		print '[*] Your access token is already stored'
		print
		print '[*] Your token'
		print
		os.system ('cat .cookie/token.log')
		print
		print
		main()
	except KeyError:
		print '[!] Failed to generate access token'
		print '[!] Check your internet connection / email or password'
		os.remove('.cookie/token.log')
		main()
	except requests.exceptions.ConnectionError:
		print '[!] Failed to generate access token'
		print '[!] Connection error !!!'
		os.remove('.cookie/token.log')
		main()
def id():
	print '[*] login to your facebook account         ';id = raw_input('[?] Gmail : ');pwd = raw_input('[?] Password : ');API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32';data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"};sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET
	x = hashlib.new('md5')
        x.update(sig)

	data.update({'sig':x.hexdigest()})
        get(data)
def main():
  global target_id

  try:
	cek = raw_input(G + 'KING' + W +' >> ')

	if cek.lower() == "cat":
		try:
			o = open('.cookie/token.log','r').read()
			print '[*] Your access token !!\n\n' + o + '\n'
			main()
		except IOError:
			print '[!] failed'
			print "[!] type 'token' to generate access token"
			main()

	elif cek.lower() == 'clear':
		if sys.platform == 'win32':
			os.system('cls')
			baliho()
			main()
		else:
			os.system('clear')
			baliho()
			main()

	elif cek.lower() == 'token':
		try:
			open('.cookie/token.log')
			print '[!] an access token already exists'
			cek = raw_input('[?] Are you sure you want to continue [Y/N] ')
			if cek.lower() != 'y' or cek.lower() != 'Y':
				print '[*] We have removed the old token '
			os.system ('rm -rf .cookie/token.log')
			main()
		except IOError:
			pass

		print '\n' + '[*] Generate Access token facebook [*]'.center(44) + '\n'
		print '[Warn] please turn off your VPN before using this feature !!!'
		id()
	elif cek.lower() == 'rm':
		print '''
[Warn] you must create access token again if 
       your access token is deleted
'''
		a = raw_input("[!] type 'delete' to continue : ")
		if a.lower() == 'delete' or a.lower() == 'Delete':
			try:
				os.system('rm -rf .cookie/token.log')
				print '[*] Success delete token'
				main()
			except OSError:
				print '[*] failed to delete token'
				main()
		else:
			print '[*] failed to delete token'
			main()
	elif cek.lower() == 'about':
		show_program()
		main()
	elif cek.lower() == 'exit':
		print "[!] Exiting Program"
		sys.exit()
	elif cek.lower() == 'help':
		info_ga()
		main()
	elif cek.lower() == 'cat':
		cat ()
	elif cek.lower() == 'y':
		y ()
	elif cek.lower() == 'f':
		f ()
	elif cek.lower() == 'g':
		g ()
	else:
		if cek == '':
			main()
		else:
			print "[!] command '"+cek+"' not found"
			print '[!] type "help" to show command'
			main()
  except KeyboardInterrupt:
	main()
  except IndexError:
	print '[!] invalid parameter on command : ' + cek
	main()

def info_ga ():

	print '''
	%sCOMMAND		DESCRIPTION%s
    -----------------        -------------------

   token		      get your token facebook
   rm         		      delete your token
   cat 			      view your token


   y			      open youtube channel  No yotube
   f			      open facebook         lutfi Binmasaleh
   g			      open github           Haiman

'''%(G,W)

def show_program ():

	print '''
                    %sINFORMATION%s
----------------------------------------------------

     Create                :  CiKu370

     Edit                  :  KING

     DateCreate            : 16/05/2018 09:35:12

     DateEdit By ZeRoNM    : 14/07/2019 09:49

'''% (G,W)

def y ():

	os.system ("xdg-open Noyoutube")
	main()

def f ():

	os.system ("xdg-open https://www.facebook.com/profile.php?id=100011409407326")
	main()

def g ():

	os.system ("xdg-open Haiman Nolink")
	main()

if __name__ == '__main__':

	baliho()
	main()

