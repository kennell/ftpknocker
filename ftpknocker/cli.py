import click
import ftplib
import multiprocessing
import random
import threading
import sys
from netaddr import IPSet
from .utils import split_list


ANONYMOUS_USER = 'anonymous'
ANONYMOUS_PASSWORD = 'anonymous'


def scan(hosts, port, timeout):
    for host in hosts:
        try:
            ftp = ftplib.FTP()
            ftp.connect(host, port, timeout)
            if '230' in ftp.login(user=ANONYMOUS_USER, passwd=ANONYMOUS_PASSWORD):
                print(host)
                ftp.quit()
        except ftplib.all_errors:
            pass


@click.command()
@click.argument('targets', nargs=-1)
@click.option('--threads', default=multiprocessing.cpu_count(), help='Number of threads to utilize')
@click.option('--port', default=21, help='Port to scan')
@click.option('--timeout', default=2.0, help='Seconds before timeout')
@click.option('--shuffle/--no-shuffle', default=False, help='Shuffle target list')
def main(targets, threads, port, timeout, shuffle):
    print(sys.version)
    if not sys.stdin.isatty():
        targets = sys.stdin.readlines()

    ipset = IPSet()
    for t in targets:
        ipset.add(t)
    ips = [str(ip) for ip in ipset]

    if shuffle:
        random.shuffle(ips)

    for chunk in split_list(ips, threads):
        threading.Thread(
            target=scan,
            kwargs={
                'hosts': chunk,
                'port': port,
                'timeout': timeout
            }
        ).start()
