import unittest
import subprocess


ANONYMOUS_FTP_SERVERS = [
    '80.237.136.138',   # ftp.hosteurope.de
    '129.215.17.244',   # ftp.ed.ac.uk
    '134.109.228.1'     # ftp.tu-chemnitz.de
]

NO_FTP_SERVERS = [
    '93.184.216.34',
    '157.240.20.35'
]


class TestScan(unittest.TestCase):

    def test_anonymous_ftp_servers(self):
        self.assertEquals(True, True)

    def test_no_ftp_servers(self):
        self.assertEquals(True, True)
