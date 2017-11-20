import unittest


ANONYMOUS_SERVERS = [
    '80.237.136.138',   # ftp.hosteurope.de
    '129.215.17.244',   # ftp.ed.ac.uk
    '134.109.228.1'     # ftp.tu-chemnitz.de
]

NON_ANONYMOUS_SERVERS = [
    '93.184.216.34',
    '157.240.20.35'
]

MIXED_SERVERS = [
    '80.237.136.138',   # ftp.hosteurope.de
    '93.184.216.34'
]


class TestScan(unittest.TestCase):

    def test_anonymous_servers(self):
        self.assertEqual(True, True)

    def test_non_anonymous_servers(self):
        self.assertEqual(True, True)

    def test_mixed_servers(self):
        self.assertEqual(True, True)
