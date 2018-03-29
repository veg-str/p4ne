from flask import Flask, jsonify
import ipaddress, re, os, json


def classify(s):
    if re.search("ip address ((?:[0-9]{1,3}\.?){4}) ((?:[0-9]{1,3}\.?){4})", s):
        x = re.match(" ip address ((?:[0-9]{1,3}\.?){4}) ((?:[0-9]{1,3}\.?){4})", s)
        return {'ip': ipaddress.IPv4Interface(str(x.group(1)) + "/" + str(x.group(2))).with_prefixlen}
    elif re.match("hostname (.+)", s):
        x = re.match("hostname (.+)", s)
        return {"host": x.group(1)}
    else:
        return {}

dir = 'c:\\Users\\ve.gusarin\\Seafile\\p4ne_training\\config_files\\'
files_list = os.listdir(dir)
os.chdir(dir)

int = []
hosts = {}


def make_lists(file_list):
    for x in files_list:
        with open(x) as f:
            ip = []
            for l in f:
                dict = classify(l)
                if 'ip' in dict: ip.append(dict['ip'])
                elif 'host' in dict: host = (dict['host'])
            hosts[host] = ip



app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return 'Hello!'

@app.route('/configs')
def configs():
#    return 'Имеются конфигурационные файлы для следующих хостов:\n'
    return jsonify(list(hosts.keys()))


@app.route('/configs/<hostname>')
def host_int(hostname):
    return jsonify(hosts[hostname])


if __name__ == '__main__':
    make_lists(files_list)
    print(hosts.keys())
    app.run(debug=True)