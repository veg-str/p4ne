import os

dir = 'c:\\Users\\ve.gusarin\\Seafile\\p4ne_training\\config_files\\'
files_list = os.listdir(dir)
os.chdir(dir)

for x in files_list:
    with open(x) as f:
        for l in f:
            if l.strip().startswith('ip address'): print(l)

