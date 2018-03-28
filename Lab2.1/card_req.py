import requests, pprint, json, argparse
file = 'C:\\Users\\ve.gusarin\\PycharmProjects\\p4ne\\Lab2.1\\card1.json'
parser = argparse.ArgumentParser()
parser.add_argument('file_name')
args = parser.parse_args()

def card_req(card_num):
    r = requests.get('https://lookup.binlist.net/' + str(card_num)[0:8], headers={'Accept-Version': "3"})
    if (200 <= r.status_code <= 299) and r.json()['bank']:
        print('Card No:', card_num)
        print(r.json()['bank'])
        return r.json()['bank']['name']
#    else:
#        pprint.pprint('Card No: ', card_num, ' error ', r.status_code)

card_nums = []
with open(args.file_name) as f:
    l = json.load(f)
    for i in l:
        card_nums.append(str(i['CreditCard']['CardNumber']))

#print(args.file_name)
banks = set()
for i in card_nums:
    banks.add(card_req(i))

pprint.pprint(banks)