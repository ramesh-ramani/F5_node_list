from f5.bigip import ManagementRoot
import certifi
import urllib3
import requests
import re

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
x_file = open('/usr/local/bin/python_scripts/nodes1.txt', 'r')

# Connect to the BigIP
mgmt = ManagementRoot("ip_address", "username", "password")

# Get a list of all pools on the BigIP and print their names and their
# members' names
test=list()
pools = mgmt.tm.ltm.pools.get_collection()
for pool in pools:
#    print pool.name
    for member in pool.members_s.get_collection():
        y=re.findall('^.+00[0-9]|^.+Site',member.name,re.MULTILINE)
        if y[0] not in test:
           test.append(y[0])

for i in test:
    print i
