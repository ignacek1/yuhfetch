#!/usr/bin/python3
import distro
import subprocess
import sys
import os

black = '\033[0;30m'
red = '\033[0;31m'
green = '\033[0;32m'
yellow = '\033[0;33m'
blue = '\033[0;34m'
purple = '\033[0;35m'
cyan = '\033[0;36m'
white = '\033[0;37m'
NC = '\033[0m'

if os.path.exists("./version.txt"):
    with open("./version.txt") as vfile:
        v = vfile.read().strip()
else:
    with open("/etc/yuhfetch/version") as vfile:
        v = vfile.read().strip()

if len(sys.argv) > 1 and sys.argv[1] == "-v" or len(sys.argv) > 1 and sys.argv[1] == "--version":
    print(v)
elif len(sys.argv) > 1 and "--noasciiart" in sys.argv[1]:
    print(f"{purple}Distro:{NC} {distro.name()}")
    print(f"{blue}Kernel: {NC}{subprocess.getoutput('uname -s -r')}")
    print(f"{green}Username: {NC}{subprocess.getoutput('whoami')}")
    print(f"{red}Hostname: {NC}{subprocess.getoutput('hostname')}")
elif len(sys.argv) > 1 and "--asciiartonly" in sys.argv[1]:
    print("    .--.")
    print(f"   |o_o |")
    print(f"   |:{yellow}_{NC}/{NC} |")
    print(f"  //   \ \ ")
    print(f"/'\_   _/`\\ ")
    print(f"\\{yellow}___{NC})=({yellow}___{NC}/")
elif len(sys.argv) > 1 and "--help" or len(sys.argv) > 1 and "-h":
    print("""-v and --version: prints the version, needs yuhfetch to be installed with make or be in the yuhfetch's src directory.
--noasciiart: prints the data with no ascii art
--asciiartonly: prints only the ascii art with no data""")
else:
    print("    .--.")
    print(f"   |o_o |    {purple}Distro:    {NC}{distro.name()}")
    print(f"   |:{yellow}_{NC}/{NC} |    {blue}Kernel:    {NC}{subprocess.getoutput('uname -s -r')}")
    print(f"  //   \ \   {green}Username:  {NC}{subprocess.getoutput('whoami')}")
    print(f"/'\_   _/`\\  {red}Hostname:  {NC}{subprocess.getoutput('hostname')}")
    print(f"\\{yellow}___{NC})=({yellow}___{NC}/")
