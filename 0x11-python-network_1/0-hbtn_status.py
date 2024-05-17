#!/usr/bin/python3
"""script fetches https://alx-intranet.hbtn.io/status"""
import urllib.request as url_req

req = url_req.Request('https://alx-intranet.hbtn.io/status')
with url_req.urlopen(req) as response:
    the_page = response.read()

decoded_content = the_page.decode('utf-8')
print('Body response:')
print('\t- type:', type(the_page))
print('\t- content:', the_page)
print('\t- utf8 content:', decoded_content)
