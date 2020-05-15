import sys, os
import subprocess 
from local_data import *

try:
	# Arguments found
	sys.argv[1] == "0"
except:
	# No arguments found so therefore print info on how to use script
	print("This program requires arguments:")
	print("	0: Toggle the VPN")
	print("	1: Check the VPN")
	sys.exit(0) # exit program

# this statement toggles the vpn
if sys.argv[1] == "0":
	# this code updates the lock file to be in sync with the connection
	status = str(subprocess.getstatusoutput("ifconfig -a | grep tun0"))
	status = status.split(",")
	
	# if the vpn is on, turn it off & vice versa
	if status[0] != '(1':
		cmd = "nmcli con down id " + vpn_name + " >> /tmp/vpn_status"
		os.system(cmd)
		new_status = '0'
	else:
		cmd = "nmcli con up id " + vpn_name + " >> /tmp/vpn_status"
		os.system(cmd)
		new_status = '1'

	file = open("vpn_status", "w")
	file.write(new_status)
	sys.exit(0)




