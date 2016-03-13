import csv, subprocess, sys

with open("New Accounts.csv", "r") as f:
	reader = csv.reader(f, delimiter=',', quotechar='"')
	for line in reader:
		
		arg = str(sys.argv[1])

		group = line[3]
		string = line[0]
		phoneExt = line[2]
		offNum = line[1]

		string = string.split(',')
		userName = string[1][:2] + string[0].lower()
		userName = userName.lsplit()
		string = string[1]+' '+string[0]
		name = string 

		if arg == '-d':
			subprocess.call(['userdel', 'userName'])
			sys.exit()

		subprocess.call(["groupadd",group])

		if group == "Engineering":
			subprocess.call(["useradd",'-d','/home/engineering/'+userName,'-g',group,'-s','/bin/csh','-c',name+', '+offNum+', '+phoneExt,userName,
			'-p','letmein'])
		else:
			subprocess.call(["useradd",'-d','/home/'+group.lower()+'/'+userName,'-g',group,'-s','/bin/bash','-c',name+', '+offNum+', '+phoneExt,userName,
			'-p','letmein'])