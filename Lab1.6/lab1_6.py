import ipaddress, re, os


def classify(s):
    if re.search("ip address ((?:[0-9]{1,3}\.?){4}) ((?:[0-9]{1,3}\.?){4})", s):
        x = re.match(" ip address ((?:[0-9]{1,3}\.?){4}) ((?:[0-9]{1,3}\.?){4})", s)
        return {'ip': ipaddress.IPv4Interface(str(x.group(1)) + "/" + str(x.group(2))).with_prefixlen}
    elif re.match("interface (.+)", s):
        x = re.match("interface (.+)", s)
        return {"int": x.group(1)}
    elif re.match("hostname (.+)", s):
        x = re.match("hostname (.+)", s)
        return {"host": x.group(1)}
    else:
        return {}

dir = 'c:\\Users\\ve.gusarin\\Seafile\\p4ne_training\\config_files\\'
files_list = os.listdir(dir)
os.chdir(dir)

ip = []
int = []
hosts = []

for x in files_list:
    with open(x) as f:
        for l in f:
            dict = classify(l)
            if 'ip' in dict: ip.append(dict)
            elif 'int' in dict: int.append(dict)
            elif 'host' in dict: hosts.append(dict)



print(ip)
print(int)
print(hosts)
#pprint.pprint(ip)
#pprint.pprint(int)
#pprint.pprint(hosts)
