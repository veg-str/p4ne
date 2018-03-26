import ipaddress, openpyxl, re, os

dir = 'c:\\Users\\ve.gusarin\\Seafile\\p4ne_training\\config_files\\'
files_list = os.listdir(dir)
os.chdir(dir)

ip = []
ipplan_item = {}
ipplan = []


def classify(s):
    if re.search("ip address ((?:[0-9]{1,3}\.?){4}) ((?:[0-9]{1,3}\.?){4})", s):
        x = re.match(" ip address ((?:[0-9]{1,3}\.?){4}) ((?:[0-9]{1,3}\.?){4})", s)
        return str.strip(x.group(1)) + "/" + str.strip(x.group(2))
    else:
        return False


for x in files_list:
    with open(x) as f:
        for l in f:
            net = classify(l)
            if net != False: ip.append(ipaddress.IPv4Interface(net))

ip = sorted(list(set(ip)))

for i in ip:
    ipplan.append({'net':str(i.network.network_address), 'mask':str(i.netmask), 'gw':str(i.ip)})


print('{:<30}'.format('Сеть'), '{:<30}'.format('Маска'), '{:<30}'.format('Шлюз'))
for i in ipplan:
    print('{:<30}'.format(i.get('net')), '{:<30}'.format(i.get('mask')), '{:<30}'.format(i.get('gw')))

wb = openpyxl.Workbook()
ws = wb.active
ws.title = 'IP Plan'




