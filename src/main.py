#!/usr/bin/python3
import distro
import subprocess

black = '\033[0;30m'
red = '\033[0;31m'
green = '\033[0;32m'
yellow = '\033[0;33m'
blue = '\033[0;34m'
purple = '\033[0;35m'
cyan = '\033[0;36m'
white = '\033[0;37m'
NC = '\033[0m'

print("    .--.")
print(f"   |o_o |    {purple}Distro:    {NC}{distro.name()}")
print(f"   |:_/ |    {blue}Kernel:    {NC}{subprocess.getoutput('uname -s -r')}")
print(f"  //   \ \   {green}Username:  {NC}{subprocess.getoutput('whoami')}")
print(f"/'\_   _/`\\  {red}Hostname:  {NC}{subprocess.getoutput('hostname')}")
print(f"\\___)=(___/")
