#!/usr/bin/env python2
import eventlet
from eventlet.green import ftplib
from argparse import ArgumentParser
from netaddr import IPSet
from random import shuffle

def tryFtpConnect(host):
	ftp = ftplib.FTP()
	try:
		ftp.connect(host=host, timeout=args.timeout)
		if '230' in ftp.login():
			print host
		ftp.quit()
	except ftplib.all_errors:
		if args.verbose:
			print host+" FAIL"
		else:
			pass

def main():
	# Parse commandline arguments
	global args
	argparser = ArgumentParser()
	argparser.add_argument('targets', nargs='+')
	argparser.add_argument('-t', '--threads',
		action='store', default=20, type=int, dest='maxThreads', help='number of threads to use, default is 20')
	argparser.add_argument('-w', '--wait',
		action='store', default=1, type=int, dest='timeout', help='seconds before timeout')
	argparser.add_argument('-s', '--shuffle',
		action='store_true', default=False, dest='shuffle', help='shuffle the target list')
	argparser.add_argument('-v', '--verbose', 
		action='store_true', default=False, dest='verbose', help='verbose behaviour')
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

	# check shuffle argument
	if args.shuffle:
		shuffle(targetlist)

	# Create and start green thread pool
	pool = eventlet.GreenPool()
	pool.resize(args.maxThreads)
	for target in targetlist:
		pool.spawn(tryFtpConnect, target)
	pool.waitall()

if __name__ == "__main__":
    main()
