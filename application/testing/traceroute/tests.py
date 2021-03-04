# -*- coding: utf-8 -*-
'''
TEST THE TRACEROUTE MODEL
'''
# Import required packages
from application.testing.tests_base import BaseTestCase
from application.models.traceroute import parse_traceroute


'''
RAW TESTS
'''
class TraceRawTests(BaseTestCase):
    def test_traces_parsed(self):
        '''
        Use a raw input to check logic for parsing
        '''
        raw_input = '''
    traceroute to 8.8.8.8 (8.8.8.8), 64 hops max, 52 byte packets
 1  192.168.50.1 (192.168.50.1)  2.000 ms  3.682 ms  2.181 ms
 2  96.120.90.5 (96.120.90.5)  10.427 ms  11.008 ms  9.749 ms
 3  po-301-1204-rur02.sanrafael.ca.sfba.comcast.net (68.86.249.181)  10.205 ms  10.704 ms  12.297 ms
 4  po-2-rur01.sanrafael.ca.sfba.comcast.net (69.139.199.141)  9.903 ms  17.299 ms  11.430 ms
 5  be-207-rar01.rohnertpr.ca.sfba.comcast.net (68.85.57.233)  11.025 ms  11.695 ms  20.080 ms
 6  be-297-ar01.santaclara.ca.sfba.comcast.net (96.108.99.13)  13.955 ms  13.398 ms  17.495 ms
 7  96.112.146.22 (96.112.146.22)  20.149 ms  13.523 ms
    96.112.146.26 (96.112.146.26)  14.994 ms
 8  10.252.217.222 (10.252.217.222)  14.555 ms
    10.252.214.254 (10.252.214.254)  15.725 ms
    10.252.73.254 (10.252.73.254)  13.425 ms
 9  dns.google (8.8.8.8)  14.790 ms  13.630 ms  13.140 ms
        '''

        # Parse the raw string
        output = parse_traceroute(raw_input)

        # Assert that the 8th hop, which is more complex, was successfully parsed
        self.assertEqual(output[8], [14.555, 15.725, 13.425])