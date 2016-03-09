import os

routerIP ="192.168.10.254"
localIP = "192.168.10.1"
remoteIP = "8.8.8.8"
remoteHostname = "google.com"

def respond(r):
	if r == 0:
		print("Success\n")
	else:
  		print("Failure\n")

def ping(target, targetType):
	print("Pinging "+targetType+"...")
	respond(os.system("ping -c 1 " + target + " -W 1 > /dev/null"))

# Test Router
ping(routerIP, "router")
# Test Local
ping(localIP, "local client")
# Test Remote IP
ping(remoteIP, "Google\'s DNS server")
# Test Remote Hostname
ping(remoteHostname, "Google.com")