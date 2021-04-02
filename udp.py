#!/usr/bin/python2
import os
import time
import sys
import argparse
import platform
import subprocess as sp
import datetime
from datetime import datetime
import socket

def banner():
    print(" _   _     _        ______          _        _     _____                _ ") 
    print("| | | |   | |       | ___ \        | |      | |   /  ___|              | |")
    print("| | | | __| |_ __   | |_/ /_ _  ___| | _____| |_  \ `--.  ___ _ __   __| |")
    print("| | | |/ _` | '_ \  |  __/ _` |/ __| |/ / _ \ __|  `--. \/ _ \ '_ \ / _` |")
    print("| |_| | (_| | |_) | | | | (_| | (__|   <  __/ |_  /\__/ /  __/ | | | (_| |")
    print(" \___/ \__,_| .__/  \_|  \__,_|\___|_|\_\___|\__| \____/ \___|_| |_|\__,_|")
    print("            | |                                                           ")
    print("            |_|                                                           ")
    print("                                                                     6AI-L")

banner()
parser=argparse.ArgumentParser()
parser.add_argument("-d", dest="dst", help="packet's target")
parser.add_argument("-p", dest="port", help="port number")
parser.add_argument("-i", dest="intensity", default=10, help="packet is being sent in every N sec. (default=10)")
insert=parser.parse_args()
UDP_IP=insert.dst
UDP_PORT=insert.port
feq=insert.intensity
i=1

while True:    
    try:    
        MESSAGE="nothing" #it is required, but the content doesn't matter... 
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(MESSAGE, (str(UDP_IP), int(UDP_PORT)))
        sys.stdout.write(str("\r%i") % i+" packet(s) sent to "+str(UDP_IP)+"!")
        sys.stdout.flush()
        time.sleep(int(feq))
        i=i+1
        
    except TypeError:
        print("usage: udp [-h] [-c DESTINATION] [-p PORT] [-i INTENSITY]")
        print("arguments:")
        print("  -h, --help     shows the help messages")
        print("  -d DST         packet's target (destination of the packet)")
        print("  -p PORT        port number")
        print("optional argument: ")
        print("  -i INTENSITY   packet is being sent in every N sec. (default=10)")  
        break
    except KeyboardInterrupt:
        print("\n")
        break
        
