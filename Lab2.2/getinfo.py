from flask import Flask
import glob,re,ipaddress

LOG_PATH="C:\\Users\\utkinia\\Documents\\Python\\config_files"

def str_to_ip(ipstr):
    if re.search("ip address", ipstr):
        net_objects = re.search("([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}) ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})", ipstr)
        if net_objects:
            addr = ipaddress.IPv4Interface(net_objects.groups())
            return addr
        else:
            return None
    else:
        return None

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return ("Этот небольшой веб-сервер показывает IP-адреса и маски в структуре REST API<br>\
            По /configs выводится список хостнеймов<br>\
            По /config/&lt;hostname&gt; - IP-адреса хоста")

@app.route('/configs')
def page1():
    return '<br>'.join(hosts.keys())

@app.route('/config/<name>')
def page2(name):
    return '<br>'.join(hosts[name])


hosts={}
for i in glob.glob(LOG_PATH+"\\*.log"):
    all_address = []
    f = open(i)
    for j in f:
        if re.search("^ *(sysname|hostname)", j):
            hostname=j.split()[1]
        a = str_to_ip(j)
        if a:
            all_address.append(str(a))
    hosts[hostname]=all_address

if __name__ == '__main__':
    app.run(debug=True)