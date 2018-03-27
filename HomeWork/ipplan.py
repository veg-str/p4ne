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
ws.cell(1, 1, 'Сеть').style = openpyxl.styles.NamedStyle = 'Headline 2'
ws.cell(1, 2, 'Маска').style = openpyxl.styles.NamedStyle = 'Headline 2'
ws.cell(1, 3, 'Шлюз').style = openpyxl.styles.NamedStyle = 'Headline 2'
ws.column_dimensions['A'].width = 20
ws.column_dimensions['B'].width = 20
ws.column_dimensions['C'].width = 20

for i in ipplan:
    a = 1
    for y in i:
        ws.cell(ipplan.index(i) + 2, a, i[y])
        a = a + 1
wb.save('C:\\Users\\ve.gusarin\\PycharmProjects\\p4ne\\HomeWork\\ipplan_veg.xlsx')