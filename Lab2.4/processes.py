import requests,pandas,flask

HOST_IP='10.31.70.209'
LOGIN='restapi'
PASSWORD='j0sg1280-7@'
HEADERS = {
    "accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}
URL='/restconf/data/Cisco-IOS-XE-process-memory-oper:memory-usage-processes'
PROTO='https://'

requests.packages.urllib3.disable_warnings()

app = flask.Flask(__name__)
app.json.sort_keys = False
@app.route('/')
@app.route('/index')
def index():
    return ("Этот небольшой веб-сервер показывает топ 10 процессов<br>\
            жрущих память какой-то непонятной железки с IP "+HOST_IP+" <br>\
            По /processes - выводится список")

@app.route('/processes')
def page1():
    r = requests.get(PROTO + HOST_IP + URL, auth=(LOGIN, PASSWORD), headers=HEADERS, verify=False)
    sorted_list = sorted(r.json()['Cisco-IOS-XE-process-memory-oper:memory-usage-processes'] \
                             ['memory-usage-process'], key=lambda x: int(x['allocated-memory']), reverse=True)
    top_dict = sorted_list[0:9]
    top_list = []
    for i in top_dict:
        top_list.append({'pid':i['pid'], 'name':i['name'], 'memory':i['allocated-memory']})
    return flask.jsonify({"top 10 processes": top_list})

if __name__ == '__main__':
    app.run(debug=True)