import unittest
from ftpknocker.utils import targets_to_ip_list


SINGLE_IP = ('44.33.22.11',)
MULTIPLE_IPS = ('11.11.11.11', '22.22.22.22', '33.33.33.33')
SINGLE_CIDR = ('188.44.22.30/24',)
MULTIPLE_CIDR = ('188.44.22.30/24', '80.12.9.104/20',)
SINGLE_CIDR_AND_SINGLE_IP = ('170.15.103.4/24', '8.8.8.8')


class TestTargetParsing(unittest.TestCase):

    def test_single_ip(self):
        ips = targets_to_ip_list(SINGLE_IP)
        self.assertEqual(len(ips), 1)

    def test_multiple_ips(self):
        ips = targets_to_ip_list(MULTIPLE_IPS)
        self.assertEqual(len(ips), 3)

    def test_single_cidr(self):
        ips = targets_to_ip_list(SINGLE_CIDR)
        self.assertEqual(len(ips), 256)

    def test_multple_cidr(self):
        ips = targets_to_ip_list(MULTIPLE_CIDR)
        self.assertEqual(len(ips), 4352)

    def test_single_cidr_and_single_ip(self):
        ips = targets_to_ip_list(SINGLE_CIDR_AND_SINGLE_IP)
        self.assertEqual(len(ips), 257)
