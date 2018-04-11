#! /usr/bin/env python
from socket import *
import sys, time
from datetime import datetime

host = ''
max_port = 5000
min_port = 1

try:
	host = raw_input("[*] Enter Target Host Address: ")
except KeyboardInterrupt:
	print("\n\n[*] User Requested An Interrupt.")
	print("[*] Application Shutting Down.")
	sys.exit(1)