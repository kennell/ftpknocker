ftpknocker
==========

ftpknocker is a fast, concurrent-connection scanner for finding anonymous FTP servers.

Requirements
------------

The **netaddr** and **eventlet** modules must be installed, on Debian/Ubuntu systems simply run:

```
sudo apt-get install python-pip python-dev
sudo pip install netaddr eventlet
```

ftpknocker was created for Python 2.x. Due to dependencies, it does not run on 3.x versions.


Usage
-----

```
usage: ftpknocker.py [-h] [-c MAXCONNECTIONS] [-t TIMEOUT] [-s]
                     targets [targets ...]

positional arguments:
  targets

optional arguments:
  -h, --help            show this help message and exit
  -c MAXCONNECTIONS, --connections MAXCONNECTIONS
                        Number of concurrent connections, default is 100
  -t TIMEOUT, --timeout TIMEOUT
                        Seconds to wait before timeout, default is 5
  -s, --shuffle         Shuffle the target list
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

Performance
--------

Performance depends largely on your Internet connection. 100 concurrent connections is the default and should work fine in most cases. On a good connection (for example, a VPS) you may be able to run with 1000-2000 connections before the network becomes unreliable.