#!/usr/bin/python3
import os, subprocess, datetime
from time import sleep

current_quarter = ((datetime.datetime.now().month - 1) // 3) + 1

file_path = "/root/Documents/Q" + str(current_quarter) + "_PCI_Wireless_" + str(datetime.datetime.now().year)
print(file_path)
if not os.path.exists(file_path):
	os.makedirs(file_path)
os.chdir(file_path)	

scan_name = raw_input("What location are you scanning?  ")
scan_name = scan_name.lower().replace(" ", "_")

interface_name = raw_input("What is the interface you will be using?  ")

if not os.path.exists(scan_name):
	os.makedirs(scan_name)

os.chdir(scan_name)
print(os.getcwd())

print subprocess.check_output(['rfkill', 'unblock', 'all'])
print("Unblock all complete")

print subprocess.check_output(['airmon-ng', 'check', 'kill'])
print("Stopped all innocuous processes")

print subprocess.check_output(['iwconfig', interface_name, 'mode', 'monitor'])
print("Interface " + interface_name + " now in Monitor Mode")

print subprocess.check_output(['ifconfig', interface_name, 'up'])
print("Interface " + interface_name + " now on")

#print subprocess.check_output(['kismet_server', '-t', scan_name, '-c', interface_name])
command = "gnome-terminal -e \"kismet_server -t \"" + scan_name + "\" -c " + interface_name + "\""
print (command)
os.system(command)

sleep(3)
os.system("kismet_client") 