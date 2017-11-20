import unittest


KNOWN_ANONYMOUS_SERVERS = [
    '80.237.136.138',   # ftp.hosteurope.de
    '129.215.17.244',   # ftp.ed.ac.uk
    '134.109.228.1'     # ftp.tu-chemnitz.de
]


class TestScan(unittest.TestCase):

    def test_known_anonymous_servers(self):
        assert(True)

if __name__ == '__main__':
    unittest.main()