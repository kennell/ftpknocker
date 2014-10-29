#!/usr/bin/env python3
from argparse import ArgumentParser
from netaddr import IPSet
from random import shuffle
from time import sleep
import ftplib
import threading

def split_list(l, parts):
        newlist = []
        splitsize = 1.0/parts*len(l)
        for i in range(parts):
                newlist.append(l[int(round(i*splitsize)):int(round((i+1)*splitsize))])
        return newlist

def tryFtpConnect(host):	
	ftp = ftplib.FTP()
	try:
		ftp.connect(host=host, timeout=args.timeout)
		if '230' in ftp.login():
			print(host)
			ftp.quit()
	except ftplib.all_errors:
		pass

argparser = ArgumentParser()
argparser.add_argument('targets', nargs='+')
argparser.add_argument('-t', '--threads',
                        action='store', default=20, type=int, dest='maxThreads', help='number of threads to use, default is 20')
argparser.add_argument('-w', '--wait',
                        action='store', default=2, type=int, dest='timeout', help='seconds to wait before timeout, default is 2')
argparser.add_argument('-s', '--shuffle',
                        action='store_true', default=False, dest='shuffle', help='shuffle the target list')
# TODO: add option for specifing a file with hosts
# argparser.add_argument('-f', '--file',
#                        action='store', dest='hostlist', help='optional file with target hosts')
args = argparser.parse_args()

# add the given target arguments to a IPSet
targetIPSets = IPSet()
for target in args.targets:
	targetIPSets.add(target)

# render the IPSet to a list with individual IPs
targetlist = list()
for ip in targetIPSets:
	targetlist.append(str(ip))

if args.shuffle:
	shuffle(targetlist)

for host in targetlist:
	while(threading.activeCount() >= args.maxThreads):
		sleep(0.1)
	threading.Thread(target=tryFtpConnect, args=(host,)).start()


