#!/usr/bin/env python3
from argparse import ArgumentParser
from netaddr import IPSet
import ftplib
import threading

argparser = ArgumentParser()
argparser.add_argument('targets', nargs='+')
argparser.add_argument('-t', '--threads',
                        action='store', default=20, type=int, dest='maxThreads', help='number of threads to use, default is 20')
argparser.add_argument('-w', '--wait',
                        action='store', default=2, type=int, dest='timeout', help='seconds to wait before timeout, default is 2')
# TODO: add option for specifing a file with hosts
# argparser.add_argument('-f', '--file',
#                        action='store', dest='hostlist', help='optional file with target hosts')
args = argparser.parse_args()

# add the given targets to a IPSet
targetIPSets = IPSet()
for target in args.targets:
	targetIPSets.add(target)

# render the IPSet to a list with individual IPs
targetlist = list()
for ip in targetIPSets:
	targetlist.append(str(ip))

def tryFtpConnect(host):	
	ftp = ftplib.FTP()
	try:
		ftp.connect(host=host, timeout=args.timeout)
		if '230' in ftp.login():
			print(host)
			ftp.quit()
	except ftplib.all_errors:
		print(host + " ERROR")


for host in targetlist:
	while(threading.activeCount() >= args.maxThreads):
		continue
	threading.Thread(target=tryFtpConnect, args=(host,)).start()
