
def parse(message):
    # print(message)
    intent, tmp = message.split('(')[0], message.split('(')[1][0:-1]
    slot = dict()
    tmp = tmp.strip().split(',')
    # print(tmp)
    for item in tmp:
        temp = item.split('=')
        if len(temp) < 2:
            continue
        slot[temp[0].strip()] = temp[1].strip()
    return intent, slot

def normalize(num, operation):
    res = ''
    for item in operation.split(';'):
        res += '\t' * num + item.strip() +'\n'
    return res
# print(parse('buy(a=1,b=2)'))
# print(normalize(1,"fruit_type = slot['fruit_type'] ; weight = slot['weight']; unit_price = slot['unit_price']; money = int(slot['unit_price']) * int(slot['weight'])"))


