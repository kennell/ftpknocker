ftpknocker
==========

ftpknocker is a fast, multi-threaded scanner for finding anonymous FTP servers

Usage
-----

```
usage: ftpknocker.py [-h] [-t MAXTHREADS] [-w TIMEOUT] targets [targets ...]

positional arguments:
  targets

optional arguments:
  -h, --help            show this help message and exit
  -t MAXTHREADS, --threads MAXTHREADS
                        number of threads to use
  -w TIMEOUT, --wait TIMEOUT
                        seconds to wait before timeout
```

Examples
--------

Scan the three specified IPs:
```
./ftpknocker.py 192.168.1.1 192.168.1.2 192.168.1.3
```

Scan an entire CIDR IP-block (a total of 254 hosts):
```
./ftpknocker.py 192.168.1.0/24
```



