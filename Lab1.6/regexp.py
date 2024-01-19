import re

m = re.match("^ip address ((?:[0-9]{1,3}\.?){4}) ((?:[0-9]{1,3}\.?){4})", "ip address 8.8.8.4 255.255.255.255")
print(m.groups())