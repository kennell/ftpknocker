#!/usr/bin/env python2
from __future__ import print_function
import eventlet
from eventlet.green import ftplib
from argparse import ArgumentParser
from netaddr import IPSet
from random import shuffle

# Try anonymous FTP login
def try_ftp_login(host):
	try:
		ftp = ftplib.FTP()
		ftp.connect(host=host, timeout=args.timeout)
		if '230' in ftp.login():
			return host
		ftp.quit()
	except ftplib.all_errors:
		return None

# Setup Argument parser
argparser = ArgumentParser()
argparser.add_argument('targets', 
	nargs='+')
argparser.add_argument('-c', '--connections',
	action='store', 
	default=100, 
	type=int, 
	dest='maxConnections', 
	help='Number of concurrent connections, default is 100')
argparser.add_argument('-t', '--timeout',
	action='store', 
	default=5, 
	type=int, 
	dest='timeout', 
	help='Seconds to wait before timeout, default is 5')
argparser.add_argument('-s', '--shuffle',
	action='store_true', 
	default=False, 
	dest='shuffle', 
	help='Shuffle the target list')
args = argparser.parse_args()

# Add  given target arguments to IPSet
targetIPSet = IPSet()
for target in args.targets:
	targetIPSet.add(target)

# Render IPSet to list
targetlist = list()
for ip in targetIPSet:
	targetlist.append(str(ip))

# Check for shuffle argument
if args.shuffle:
	shuffle(targetlist)

# Create and dispatch eventlet workers
workers = eventlet.GreenPool(args.maxConnections)
for res in workers.imap(try_ftp_login, targetlist):
	if res:
		print (res)