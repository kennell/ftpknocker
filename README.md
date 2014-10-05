ftpknocker
==========

ftpknocker is a fast, multi-threaded scanner for finding anonymous FTP servers.

Requirements
------------

The iptools module for python must be installed:

```
sudo pip install iptools
```

Usage
-----

```
usage: ftpknocker.py [-h] [-t MAXTHREADS] [-w TIMEOUT] targets [targets ...]

positional arguments:
  targets

optional arguments:
  -h, --help            show this help message and exit
  -t MAXTHREADS, --threads MAXTHREADS
                        number of threads to use, default is 20
  -w TIMEOUT, --wait TIMEOUT
                        seconds to wait before timeout, default is 2
```

Examples
--------

The syntax for specifying targets is similar to the one used in nmap. Here are some examples:

Scan the three specified IPs:
```
./ftpknocker.py 192.168.1.1 192.168.1.2 192.168.1.3
```

Scan an entire IP-block using <a href="http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation">CIDR notation</a> (in this example, all hosts from 192.168.1.1 - 192.168.1.254 will be scanned, a total of 254 hosts):
```
./ftpknocker.py 192.168.1.0/24
```

