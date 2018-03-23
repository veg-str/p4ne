import ipaddress, openpyxl, re, os


dir = 'c:\\Users\\ve.gusarin\\Seafile\\p4ne_training\\config_files\\'
files_list = os.listdir(dir)
os.chdir(dir)

def classify(s):
    if re.search("ip address ((?:[0-9]{1,3}\.?){4}) ((?:[0-9]{1,3}\.?){4})", s):
        x = re.match(" ip address ((?:[0-9]{1,3}\.?){4}) ((?:[0-9]{1,3}\.?){4})", s)
        return {'ip': ipaddress.IPv4Interface(str(x.group(1)) + "/" + str(x.group(2))).with_netmask}
    else:
        return {}

ip = []
for x in files_list:
    with open(x) as f:
        for l in f:
            dict = classify(l)
            if 'ip' in dict: ip.append(dict)

print(ip)