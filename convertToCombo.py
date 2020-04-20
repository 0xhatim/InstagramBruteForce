username = open("username.txt","r").read().splitlines()
password = open("password.txt","r").read().splitlines()

for i in username:
	for m in password:
		with open("combo.txt","a") as wr:
			wr.write(i+":"+m+'\n')
