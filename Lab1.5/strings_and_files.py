import os

dir = 'c:\\Users\\ve.gusarin\\Seafile\\p4ne_training\\config_files\\'
files_list = os.listdir(dir)
os.chdir(dir)
ip = []


for x in files_list:
    with open(x) as f:
        for l in f:
            if l.strip().startswith('ip address'):
                y = l.lstrip('ip address ').rstrip()
                ip.append(y)



ip = list(set(ip))
print(ip)